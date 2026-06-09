from rest_framework import status
from rest_framework.test import APITestCase

from app.models import Treatment, Category, MonthlyOffer


class MonthlyOfferListAPITest(APITestCase):
    url = "/api/monthly-offer/"

    @classmethod
    def setUpTestData(cls):
        category_1 = Category.objects.create(name="Gesichtsbehandlungen")
        category_2 = Category.objects.create(name="Körperhandlungen")
        treatment_1 = Treatment.objects.create(name="Gesichtsbehandlung", description="Gesichtsbehandlungen",
                                               category=category_1,
                                               price="100")
        treatment_2 = Treatment.objects.create(name="Körperbehandlung", description="Körperhandlungen",
                                               category=category_2,
                                               price="150")
        MonthlyOffer.objects.create(title="Gesichtsbehandlung", description="Angebot Gesichtsbehandlung",
                                    treatment=treatment_1, image="", price=50.00, active=False)
        MonthlyOffer.objects.create(title="Körperbehandlung", description="Angebot Körperhandlungen",
                                    treatment=treatment_2, image="", price=100.00, active=True)

    def test_list_return_200(self):
        response = self.client.get(self.url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_list_offers(self):
        response = self.client.get(self.url)
        self.assertEqual(len(response.data), 2)
        self.assertFalse(response.data[0]["active"])
        self.assertTrue(response.data[1]["active"])

    def test_list_response_shape(self):
        response = self.client.get(self.url)

        self.assertIn("title", response.data[0])
        self.assertIn("description", response.data[0])
        self.assertIn("price", response.data[0])


class MonthlyOfferListEmptyAPITest(APITestCase):
    url = "/api/monthly-offer/"

    def test_list_empty_when_no_offers(self):
        MonthlyOffer.objects.all().delete()

        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 0)
