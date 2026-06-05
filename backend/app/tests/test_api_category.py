from rest_framework import status
from rest_framework.test import APITestCase

from app.models import Category


class CategoryListAPITest(APITestCase):
    url = "/api/category/"

    @classmethod
    def setUpTestData(cls):
        Category.objects.create(name="Gesichtsbehandlungen")
        Category.objects.create(name="Körperbehandlungen")
        Category.objects.create(name="Nagäldesign")

    def test_list_return_200(self):
        response = self.client.get(self.url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_list_list_categories(self):
        response = self.client.get(self.url)
        self.assertEqual(len(response.data), 3)

    def test_list_response_shape(self):
        response = self.client.get(self.url)
        self.assertIn("id", response.data[0])
        self.assertIn("name", response.data[0])

    def test_list_ordered_by_name(self):
        response = self.client.get(self.url)
        names = [item["name"] for item in response.data]

        self.assertEqual(names, sorted(names))


class CategoryListEmptyAPITest(APITestCase):
    url = "/api/category/"

    def test_list_empty_when_no_categories(self):
        Category.objects.all().delete()

        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 0)
