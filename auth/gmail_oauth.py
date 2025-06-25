
import os
import sys
import json
import requests
from pathlib import Path
import imaplib2
from dotenv import load_dotenv
import google.auth.transport.requests
from google_auth_oauthlib.flow import InstalledAppFlow
from google.oauth2.credentials import Credentials
from google.auth.transport.requests import Request

SCOPES = [
    "https://mail.google.com/",
    "openid",
    "https://www.googleapis.com/auth/userinfo.email"
]

# Support PyInstaller .exe path
BASE_DIR = Path(getattr(sys, '_MEIPASS', Path(__file__).parent))
CLIENT_SECRET_PATH = BASE_DIR / "client_secret.json"
TOKEN_PATH = Path(__file__).parent / "token.json"
ENV_PATH = Path(__file__).parent.parent / ".env"

def get_user_email_from_token(creds):
    try:
        headers = {"Authorization": f"Bearer {creds.token}"}
        resp = requests.get("https://www.googleapis.com/oauth2/v2/userinfo", headers=headers)
        resp.raise_for_status()
        return resp.json().get("email")
    except Exception as e:
        print("[ERROR] Failed to retrieve email from token:", e)
        return None

def get_gmail_connection():
    if ENV_PATH.exists():
        load_dotenv(ENV_PATH)

    fallback_email = os.getenv("EMAIL")
    creds = None

    if TOKEN_PATH.exists():
        creds = Credentials.from_authorized_user_file(TOKEN_PATH, SCOPES)

    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                str(CLIENT_SECRET_PATH),
                SCOPES
            )
            creds = flow.run_local_server(port=0)
        with open(TOKEN_PATH, "w") as token:
            token.write(creds.to_json())

    if not creds or not creds.valid or not creds.token:
        raise Exception("OAuth2 credentials are invalid or missing")

    user_email = None
    if hasattr(creds, 'id_token') and isinstance(creds.id_token, dict):
        user_email = creds.id_token.get("email")
    if not user_email:
        user_email = get_user_email_from_token(creds)
    if not user_email:
        user_email = fallback_email

    print("[DEBUG] OAuth2 Email:", user_email)
    print("[DEBUG] Access Token (start):", creds.token[:10], "...")

    if not user_email:
        raise Exception("Unable to determine authenticated user's email")

    auth_string = f"user={user_email}\1auth=Bearer {creds.token}\1\1"
    connection = imaplib2.IMAP4_SSL("imap.gmail.com")
    try:
        connection.authenticate("XOAUTH2", lambda x: auth_string.encode())
        connection.select("inbox")
    except Exception as e:
        raise Exception(f"Gmail XOAUTH2 failed: {e}")
    return connection
