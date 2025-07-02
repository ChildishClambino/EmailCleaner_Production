# 📬 Gmail Email Cleaner (Production-Ready)

A desktop tool to **search, preview, and bulk delete Gmail emails** using a clean Python GUI and secure OAuth2 authentication.

![Python](https://img.shields.io/badge/Python-3.12-blue)
![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)

---

## 🚀 Features

- ✅ OAuth2 login (no password stored)
- ✅ Search by sender, subject, and date
- ✅ Preview plain-text or HTML emails
- ✅ Bulk delete or single-delete emails
- ✅ Safe Mode (prevents accidental deletes)
- ✅ Threaded UI for smooth experience

---

## 🔧 Setup Instructions

### 1. Clone the Repository
```bash
git clone https://github.com/ChildishClambino/EmailCleaner_Production.git
cd EmailCleaner_Production
```

### 2. Install Requirements
```bash
pip install -r requirements.txt
```

### 3. Add Required Files

| File                | Location       | Description                              |
|---------------------|----------------|------------------------------------------|
| `client_secret.json`| `auth/` folder | Required for Gmail OAuth2 authentication |
| `.env`              | root folder    | Set fallback email address (optional)    |

---

### ✅ Example `.env` File
```env
EMAIL=jacobgarcilazo@gmail.com
```

---

### 4. Run the App
```bash
python main.py
```

---

## 🧪 Executable (.exe) Version

To build:
```bash
pyinstaller --noconfirm --onefile --windowed --icon=icon.ico main.py
```

Steps:
1. Place `client_secret.json` in `auth/`
2. Run `main.exe`

---

## ⚠️ Security Notice

This app uses Gmail OAuth2. No passwords are stored. You can revoke access at any time from your [Google account](https://myaccount.google.com/permissions).

---

## 📄 License
MIT License — free to use, modify, and share.
