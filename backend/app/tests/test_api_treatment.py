from rest_framework import status
from rest_framework.test import APITestCase

from app.models import Treatment, Category


class GalleryListAPITest(APITestCase):
    url = "/api/treatment/"

    @classmethod
    def setUpTestData(cls):
        category_1 = Category.objects.create(name="Gesichtsbehandlungen")
        category_2 = Category.objects.create(name="Körperhandlungen")
        Treatment.objects.create(name="Gesichtsbehandlung", description="Gesichtsbehandlungen", category=category_1,
                                 price="100")
        Treatment.objects.create(name="Körperbehandlung", description="Körperhandlungen", category=category_2,
                                 price="50")

    def test_list_return_200(self):
        response = self.client.get(self.url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_list_list_images(self):
        response = self.client.get(self.url)
        self.assertEqual(len(response.data), 2)

    def test_list_response_shape(self):
        response = self.client.get(self.url)
        self.assertIn("name", response.data[0])
        self.assertIn("description", response.data[0])
        self.assertIn("price", response.data[0])


class GalleryListEmptyAPITest(APITestCase):
    url = "/api/treatment/"

    def test_list_empty_when_no_categories(self):
        Treatment.objects.all().delete()

        response = self.client.get(self.url)
        print("Response data:", response.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 0)
