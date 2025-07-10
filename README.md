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

---

## 🔐 How to Get Your `client_secret.json`

This is required to allow the app to connect securely to your Gmail account using OAuth2.

### Step-by-Step Instructions:

1. Go to the [Google Cloud Console](https://console.cloud.google.com/apis/credentials)
2. Click the dropdown at the top and select **"New Project"**
   - Name it: `Email Cleaner`
   - Click **Create**, then switch to it
3. In the left menu, go to **APIs & Services > Library**
   - Search for: **Gmail API**
   - Click **Enable**
4. In the left menu, go to **Credentials**
   - Click **Create Credentials → OAuth client ID**
   - If prompted, set up the consent screen (name: Email Cleaner, test user: your Gmail)
   - Choose **Desktop App**, name it: `EmailCleaner`
   - Click **Create**
   - Click **Download JSON**
   - Rename it to:
     ```
     client_secret.json
     ```
   - Move it to the `auth/` folder of this project

---

## ⚙️ Add `.env` File

In the root of the project, create a file named `.env`:

```env
EMAIL=youremail@gmail.com
```

This fallback email is used if token parsing fails (optional).

---

## ▶️ Run the App
```bash
python main.py
```

> You'll be prompted to log into Gmail via your browser. On success, the GUI will load and connect to your inbox.

---

## 🧪 Build Executable (Windows)
```bash
pyinstaller --noconfirm --onefile --windowed --icon=icon.ico main.py
```

Your executable will appear in:
```
dist/main.exe
```

Make sure `auth/client_secret.json` is bundled with it.

---

## 🛡 Security Note

- This app uses **OAuth2** (no stored passwords)
- You can revoke access anytime from your Google account:  
  https://myaccount.google.com/permissions

---

## 📄 License
MIT License — open-source and free to use.

---

## 👤 Author

**Jacob Garcilazo**  
GitHub: [ChildishClambino](https://github.com/ChildishClambino)
