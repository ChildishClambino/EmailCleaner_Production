
import tkinter as tk
from tkinter import messagebox, scrolledtext
import threading
import email
import re
import calendar
from datetime import datetime
from auth.gmail_oauth import get_gmail_connection

def launch_gui():
    try:
        mail = get_gmail_connection()
    except Exception as e:
        messagebox.showerror("OAuth Login Failed", f"Could not authenticate to Gmail: {e}")
        return

    root = tk.Tk()
    root.title("Email Cleaner")
    root.geometry("700x550")

    status_label = tk.Label(root, text="Connected to Gmail", fg="green")
    status_label.pack()

    sender_entry = tk.Entry(root, width=50)
    sender_entry.pack()
    sender_entry.insert(0, "From:")

    subject_entry = tk.Entry(root, width=50)
    subject_entry.pack()
    subject_entry.insert(0, "Subject contains:")

    date_frame = tk.Frame(root)
    date_frame.pack()
    day_var = tk.StringVar(value="Day")
    month_var = tk.StringVar(value="Month")
    year_var = tk.StringVar(value="Year")
    tk.OptionMenu(date_frame, day_var, *[str(i).zfill(2) for i in range(1, 32)]).pack(side="left")
    tk.OptionMenu(date_frame, month_var, *calendar.month_abbr[1:]).pack(side="left")
    tk.OptionMenu(date_frame, year_var, *[str(y) for y in range(datetime.now().year, datetime.now().year - 10, -1)]).pack(side="left")

    safe_mode = tk.BooleanVar(value=True)
    tk.Checkbutton(root, text="Safe Mode (Preview Only)", variable=safe_mode).pack()

    results_listbox = tk.Listbox(root, width=80, height=10)
    results_listbox.pack()

    preview_area = scrolledtext.ScrolledText(root, width=80, height=10, wrap=tk.WORD)
    preview_area.pack()

    uid_map = []

    def encode_uid(uid):
        return uid.decode() if isinstance(uid, bytes) else str(uid)

    def threaded_search():
        def search_emails():
            results_listbox.delete(0, tk.END)
            preview_area.delete("1.0", tk.END)
            uid_map.clear()

            query = []
            from_val = sender_entry.get().replace("From:", "").strip()
            subject_val = subject_entry.get().replace("Subject contains:", "").strip()
            if from_val:
                query += ["FROM", f'"{from_val}"']
            if subject_val:
                query += ["SUBJECT", f'"{subject_val}"']
            if day_var.get().isdigit() and month_var.get() != "Month" and year_var.get().isdigit():
                query += ["SINCE", f"{day_var.get()}-{month_var.get()}-{year_var.get()}"]

            if not query:
                messagebox.showwarning("Empty Search", "Please enter at least one filter.")
                return

            try:
                status, messages = mail.search(None, *query)
                if status != "OK":
                    status_label.config(text="Search failed", fg="red")
                    return

                email_ids = messages[0].split()
                for num in email_ids:
                    status, data = mail.fetch(num, "(UID RFC822)")
                    if status != "OK":
                        continue
                    raw_header = data[0][0].decode(errors="ignore")
                    uid_match = re.search(r"UID (\d+)", raw_header)
                    uid = uid_match.group(1) if uid_match else None
                    msg = email.message_from_bytes(data[0][1])
                    subject = msg["subject"] or "(No Subject)"
                    if uid:
                        uid_map.append((uid, subject))
                        results_listbox.insert(tk.END, subject)

                status_label.config(text=f"Found {len(uid_map)} emails.", fg="blue")
            except Exception as e:
                status_label.config(text=f"Error: {str(e)}", fg="red")

        threading.Thread(target=search_emails, daemon=True).start()

    def preview_email():
        selection = results_listbox.curselection()
        if not selection:
            return
        index = selection[0]
        uid = uid_map[index][0]

        def task():
            preview_area.delete("1.0", tk.END)
            uid_str = encode_uid(uid).strip()
            try:
                result, data = mail.uid('FETCH', uid_str.encode(), '(RFC822)')
                if result != "OK":
                    raise Exception("Failed to fetch email content")
                msg = email.message_from_bytes(data[0][1])
                preview_text = ""

                if msg.is_multipart():
                    for part in msg.walk():
                        ctype = part.get_content_type()
                        if ctype == "text/plain":
                            preview_text += part.get_payload(decode=True).decode(errors="ignore")
                        elif ctype == "text/html" and not preview_text:
                            html = part.get_payload(decode=True).decode(errors="ignore")
                            preview_text = "[HTML Fallback]\n" + re.sub(r'<[^>]+>', '', html)
                else:
                    preview_text = msg.get_payload(decode=True).decode(errors="ignore")

                preview_area.insert(tk.END, preview_text[:10000])
            except Exception as e:
                messagebox.showerror("Preview Error", f"Failed to preview email: {e}")

        threading.Thread(target=task, daemon=True).start()

    def delete_email():
        selection = results_listbox.curselection()
        if not selection:
            return
        index = selection[0]
        uid = uid_map[index][0]
        subject = uid_map[index][1]
        confirm = messagebox.askyesno("Confirm Delete", f"Are you sure you want to delete:\n{subject}")
        if confirm:
            if safe_mode.get():
                messagebox.showinfo("Safe Mode", "Safe Mode is ON — no email was deleted.")
                return
            try:
                mail.uid('STORE', uid.encode(), '+FLAGS', r'(\Deleted)')
                mail.expunge()
                results_listbox.delete(index)
                preview_area.delete("1.0", tk.END)
                del uid_map[index]
                status_label.config(text="Email deleted.", fg="red")
            except Exception as e:
                messagebox.showerror("Error", f"Failed to delete email: {e}")

    def delete_all_results():
        if not uid_map:
            return
        confirm = messagebox.askyesno("Confirm Mass Delete", f"Are you sure you want to delete ALL {len(uid_map)} emails?")
        if not confirm:
            return
        if safe_mode.get():
            messagebox.showinfo("Safe Mode", "Safe Mode is ON — no emails were deleted.")
            return
        try:
            for uid, _ in uid_map:
                mail.uid('STORE', uid.encode(), '+FLAGS', r'(\Deleted)')
            mail.expunge()
            uid_map.clear()
            results_listbox.delete(0, tk.END)
            preview_area.delete("1.0", tk.END)
            status_label.config(text="All emails deleted.", fg="red")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to delete emails: {e}")

    tk.Button(root, text="Search", command=threaded_search).pack()
    tk.Button(root, text="Preview", command=preview_email).pack()
    tk.Button(root, text="Delete", command=delete_email).pack()
    tk.Button(root, text="Delete All Results", command=delete_all_results).pack()

    def on_closing():
        try:
            mail.logout()
        except:
            pass
        root.destroy()

    root.protocol("WM_DELETE_WINDOW", on_closing)
    root.mainloop()
