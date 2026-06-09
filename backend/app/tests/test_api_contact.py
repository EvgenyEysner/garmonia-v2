from unittest.mock import patch

from rest_framework import status
from rest_framework.test import APITestCase

from app.models import Category, Treatment
from app.services.email import ResendError


class CategoryListAPITest(APITestCase):
    url = "/api/contact/"

    @classmethod
    def setUpTestData(cls):
        category = Category.objects.create(name="Gesichtsbehandlungen")
        cls.treatment = Treatment.objects.create(
            name="Bioenzyme Therapie",
            category=category,
            price="95",
        )

    def valid_payload(self):
        return {
            "name": "Max Mustermann",
            "email": "max@example.com",
            "phone": "+49 179 123456",
            "treatment_id": self.treatment.id,
            "message": "Termin am Freitag bitte",
        }

    @patch("app.views.send_contact_email")
    def test_post_valid_returns_201(self, mock_send):
        response = self.client.post(self.url, data=self.valid_payload(), format="json")

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data["message"], "Ihre Anfrage wurde gesendet.")
        mock_send.assert_called_once()

    def test_post_missing_fields_returns_400(self):
        response = self.client.post(self.url, {"treatment_id": "Max"}, format="json")
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_post_invalid_treatment_id_returns_400(self):
        payload = self.valid_payload()
        payload["treatment_id"] = 9999999999
        response = self.client.post(self.url, payload, format="json")
        
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_post_treatment_id_none_returns_400(self):
        payload = self.valid_payload()
        payload["treatment_id"] = None
        response = self.client.post(self.url, payload, format="json")

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    @patch("app.views.send_contact_email", side_effect=ResendError("API down"))
    def test_post_resend_error_returns_503(self, mock_send):
        response = self.client.post(self.url, self.valid_payload(), format="json")
        self.assertEqual(response.status_code, status.HTTP_503_SERVICE_UNAVAILABLE)
        self.assertEqual(response.data["message"], "E-Mail konnte nicht gesendet werden.")
        mock_send.assert_called_once()
