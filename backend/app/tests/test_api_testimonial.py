from rest_framework import status
from rest_framework.test import APITestCase

from app.models import Testimonial


class GalleryListAPITest(APITestCase):
    url = "/api/testimonial/"

    @classmethod
    def setUpTestData(cls):
        Testimonial.objects.create(first_name="Max", last_name="Muster", text="Alles Supppper!!!")
        Testimonial.objects.create(first_name="Max", last_name="Mustermann", text="Alles weniger Supppper!!!")

    def test_list_return_200(self):
        response = self.client.get(self.url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_list_list_images(self):
        response = self.client.get(self.url)
        self.assertEqual(len(response.data), 2)

    def test_list_response_shape(self):
        response = self.client.get(self.url)
        self.assertIn("first_name", response.data[0])
        self.assertIn("last_name", response.data[0])
        self.assertIn("text", response.data[0])

        self.assertEqual(response.data[0]["text"], "Alles Supppper!!!")

    def test_get_user_full_name(self):
        response = self.client.get(self.url)
        data = response.data[0]
        self.assertEqual(data["full_name"], "Max Muster")

    def test_list_ordered_by_last_name(self):
        response = self.client.get(self.url)
        names = [item["last_name"] for item in response.data]

        self.assertEqual(names, sorted(names))


class GalleryListEmptyAPITest(APITestCase):
    url = "/api/testimonial/"

    def test_list_empty_when_no_categories(self):
        Testimonial.objects.all().delete()

        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 0)
