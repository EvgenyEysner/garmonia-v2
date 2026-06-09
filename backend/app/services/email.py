import logging
from typing import Iterable

import requests
from django.conf import settings

from app.models import Treatment

logger = logging.getLogger(__name__)


class ResendError(RuntimeError):
    """Raised when Resend rejects a message or is unreachable."""
    ...


def send_contact_email(data: dict, recipients: Iterable[str] | None = None, reply_to: str | None = None) -> str:
    """Send a plain-text email via Resend. Returns the Resend message id.

    Configuration (settings):
        RESEND_API_KEY        required
        RESEND_FROM_EMAIL     required, must use a Resend-verified domain
        RECIPIENT_ADDRESS     default recipient when `recipients` is None
        RESEND_TIMEOUT        optional, request timeout in seconds
    """
    treatment = Treatment.objects.get(pk=data["treatment_id"])
    api_key = getattr(settings, "RESEND_API_KEY", "") or ""
    from_email = getattr(settings, "RESEND_FROM_EMAIL", "") or ""
    endpoint = (
            getattr(settings, "RESEND_ENDPOINT", "") or "https://api.resend.com/emails"
    )
    if not api_key:
        raise ResendError("RESEND_API_KEY is not configured")
    if not from_email:
        raise ResendError("RESEND_FROM_EMAIL is not configured")

    to_list = list(recipients) if recipients else [settings.RECIPIENT_ADDRESS]
    body = f"""
    Neue Terminanfrage über die Website
    Name:       {data["name"]}
    E-Mail:     {data["email"]}
    Telefon:    {data["phone"]}
    Nachricht:
    {data.get("message") or "—"}
    """
    payload: dict = {
        "from": from_email,
        "to": to_list,
        "subject": f"Gewünschte Behandlung: {treatment.name}",
        "text": body,
    }
    if reply_to:
        payload["reply_to"] = data["email"]

    try:
        response = requests.post(
            endpoint,
            json=payload,
            headers={
                "Authorization": f"Bearer {api_key}",
                "Content-Type": "application/json",
            },
            timeout=getattr(settings, "RESEND_TIMEOUT", 15),
        )
    except requests.RequestException as exc:
        raise ResendError(f"Resend request failed: {exc}") from exc

    if response.status_code >= 400:
        detail = response.text[:500]
        logger.error(f"Resend rejected message {response.status_code}, {detail}")
        raise ResendError(f"Resend returned HTTP {response.status_code}: {detail}")

    try:
        return response.json().get("id", "")
    except ValueError:
        return ""
