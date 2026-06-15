import base64
import hashlib
import os
import secrets

import requests
from django.conf import settings
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import Flow

SCOPES = ["https://www.googleapis.com/auth/business.manage"]
TOKEN_FILE = "google_token.json"  # oder in DB/Redis speichern


def generate_pkce_pair():
    """Generiert code_verifier und code_challenge für PKCE."""
    code_verifier = secrets.token_urlsafe(64)
    code_challenge = base64.urlsafe_b64encode(
        hashlib.sha256(code_verifier.encode()).digest()
    ).rstrip(b"=").decode()
    return code_verifier, code_challenge


def get_flow():
    client_config = {
        "web": {
            "client_id": getattr(settings, "GOOGLE_CLIENT_ID"),
            "client_secret": getattr(settings, "GOOGLE_CLIENT_SECRET"),
            "redirect_uris": [getattr(settings, "GOOGLE_REDIRECT_URI")],
            "auth_uri": "https://accounts.google.com/o/oauth2/auth",
            "token_uri": "https://oauth2.googleapis.com/token",
        }
    }
    return Flow.from_client_config(
        client_config,
        scopes=SCOPES,
        redirect_uri=getattr(settings, "GOOGLE_REDIRECT_URI")
    )


def get_credentials():
    """Lädt gespeicherte Credentials und erneuert sie bei Bedarf."""
    if not os.path.exists(TOKEN_FILE):
        return None

    creds = Credentials.from_authorized_user_file(TOKEN_FILE, SCOPES)

    if creds and creds.expired and creds.refresh_token:
        creds.refresh(Request())
        save_credentials(creds)

    return creds


def save_credentials(creds):
    with open(TOKEN_FILE, "w") as f:
        f.write(creds.to_json())


BASE_URL = "https://mybusiness.googleapis.com/v4"


def get_headers():
    creds = get_credentials()
    if not creds:
        raise Exception("Nicht authentifiziert. Bitte OAuth-Flow starten.")
    return {"Authorization": f"Bearer {creds.token}"}


def fetch_all_reviews():
    """Holt alle Bewertungen paginiert."""
    account_id = getattr(settings, "GOOGLE_ACCOUNT_ID", None)
    location_id = getattr(settings, "GOOGLE_LOCATION_ID", None)

    # Aus der Doku: GET /v4/accounts/{accountId}/locations/{locationId}/reviews
    # accountId und locationId sind nur die Nummern, nicht der volle Pfad
    account_num = account_id.split("/")[-1]
    location_num = location_id.split("/")[-1]

    url = f"{BASE_URL}/accounts/{account_num}/locations/{location_num}/reviews"
    all_reviews = []
    next_page_token = None

    while True:
        params = {"pageSize": 50}
        if next_page_token:
            params["pageToken"] = next_page_token

        response = requests.get(url, headers=get_headers(), params=params)
        response.raise_for_status()
        data = response.json()

        all_reviews.extend(data.get("reviews", []))
        next_page_token = data.get("nextPageToken")

        if not next_page_token:
            break

    return all_reviews
