# 📬 Gmail Email Cleaner

A desktop GUI tool for Gmail users to **search, preview, and bulk delete emails** securely using Gmail OAuth2 authentication. Built with Python and Tkinter.

---

## 🔑 Features

- ✅ OAuth2 login (Google-approved)
- ✅ Search by sender, subject, and date
- ✅ Preview plain-text or HTML content
- ✅ Delete individual or all search results
- ✅ Safe Mode to prevent accidental deletions
- ✅ Smooth, responsive GUI (threaded actions)

---

## 🖥 Tech Stack

- Python 3.12
- Tkinter (GUI)
- Google OAuth2 (no password storage)
- imaplib2
- dotenv

---

## 📦 Installation

### 1. Clone the Repository
```bash
git clone https://github.com/ChildishClambino/EmailCleaner_Production.git
cd EmailCleaner_Production
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Add Required Files

| File                | Location       | Purpose                              |
|---------------------|----------------|--------------------------------------|
| `client_secret.json`| `auth/`        | Gmail OAuth2 desktop credentials     |
| `.env`              | root folder    | Fallback email (optional)            |

### Example `.env`:
```env
EMAIL=youremail@gmail.com
```

---

## ▶️ Run the App
```bash
python main.py
```

> You'll be prompted to log into Gmail via browser.

---

## 🧪 Building the Executable (Windows)
```bash
pyinstaller --noconfirm --onefile --windowed --icon=icon.ico main.py
```

Then run:
```
dist/main.exe
```

---

## 🛡 Security Note

- This app uses **OAuth2** (no stored passwords)
- You can revoke access anytime from:  
  https://myaccount.google.com/permissions

---

## 📄 License
MIT License — open-source and free to use.

---

## 👤 Author

**Jacob Garcilazo**  
GitHub: [ChildishClambino](https://github.com/ChildishClambino)
