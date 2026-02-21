"""
Run this script locally whenever the Google OAuth token expires or is revoked.
It opens a browser for you to log in, then prints the token JSON to copy
into Vercel's GOOGLE_TOKEN environment variable.

Usage:
    python generate_token.py
"""
import json
from google_auth_oauthlib.flow import InstalledAppFlow

SCOPES = ["https://mail.google.com/"]
CREDENTIALS_FILE = "credentials.json"
TOKEN_FILE = "token.json"

flow = InstalledAppFlow.from_client_secrets_file(CREDENTIALS_FILE, SCOPES)
creds = flow.run_local_server(port=0)

token_json = creds.to_json()

with open(TOKEN_FILE, "w") as f:
    f.write(token_json)

print("\nDone. token.json updated locally.\n")
print("=" * 60)
print("Copy the value below and paste it into Vercel as GOOGLE_TOKEN:")
print("=" * 60)
print(token_json)
print("=" * 60)
print("\nVercel dashboard → your project → Settings → Environment Variables")
print("Update GOOGLE_TOKEN with the text above, then redeploy.\n")
