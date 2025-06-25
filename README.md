
# Gmail Email Cleaner (Production-Ready)

A secure, desktop email cleaner tool that connects to your Gmail inbox using OAuth2, allowing you to search, preview, and delete emails in bulk using a friendly GUI.

---

## 🔐 Security Disclaimer

This tool uses **OAuth2** via `client_secret.json`. **For your security and per Google's policy**, this file is **NOT included** in the repository and must be added manually after cloning or downloading the app.

---

## ✅ Setup Instructions (For Developers or Users)

### 1. Clone the Repository
```bash
git clone https://github.com/ChildishClambino/EmailCleaner_Production.git
cd EmailCleaner_Production
```

---

### 2. Install Requirements
```bash
pip install -r requirements.txt
```

---

### 3. Add Required Files

| File                | Location            | Description                           |
|---------------------|---------------------|---------------------------------------|
| `client_secret.json`| Root project folder | Required to authenticate with Gmail   |
| `.env`              | Root project folder | Add your email for fallback           |

#### Example `.env` file:
```
EMAIL=your_email@gmail.com
```

---

### 4. Run the App (Source Code)
```bash
python main.py
```

Or, to build the `.exe` for distribution:

```bash
pyinstaller --noconfirm --onefile --windowed --icon=icon.ico main.py
```

---

## 📦 Executable (.exe) Version

If you're using the prebuilt `.exe`:

### Required Setup:
1. Extract `main.exe` from the ZIP
2. Manually place `client_secret.json` **next to** `main.exe`
3. Double-click `main.exe` to launch the GUI

---

## 🛠 Features

- OAuth2 Gmail authentication (no password storage)
- Tkinter GUI
- Email search (by sender, subject, date)
- Single and bulk deletion
- Safe mode toggle (to preview before deleting)
- Uses threading for smooth UX

---

## 💬 Need Help?

If you're not sure how to get your `client_secret.json`, [click here to generate your credentials](https://console.cloud.google.com/apis/credentials)

---

## 📄 License

MIT (or custom — update this section if needed)
