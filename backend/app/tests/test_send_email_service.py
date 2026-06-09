from unittest.mock import patch, MagicMock

from django.test import TestCase, override_settings

from app.models import Category, Treatment
from app.services.email import send_contact_email


@override_settings(
    RESEND_API_KEY="api-key",
    RESEND_FROM_EMAIL="test@example.com",
    RECIPIENT_ADDRESS="studio@example.com",
)
class TestSendEmailService(TestCase):
    @classmethod
    def setUp(cls):
        category = Category.objects.create(name="Kosmetik")
        cls.treatment = Treatment.objects.create(
            name="Peeling", category=category
        )

    @patch("app.services.email.requests.post")
    def test_send_email(self, mock_post):
        # --- Fictitious Resend Message ID? Only relevant because the service returns response.json().get(“id”) ---
        mock_post.return_value = MagicMock(status_code=200, text='{"id":"123"}')
        mock_post.return_value.json.return_value = {"id": "123"}

        data = {
            "name": "Anna",
            "email": "anna@example.com",
            "phone": "04411234567",
            "treatment_id": self.treatment.id,
            "message": "Hallo",
        }
        result = send_contact_email(data)
        self.assertEqual(result, "123")
        payload = mock_post.call_args.kwargs["json"]
        self.assertIn("Peeling", payload["subject"])
