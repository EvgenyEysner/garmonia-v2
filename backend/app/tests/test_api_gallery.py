from rest_framework import status
from rest_framework.test import APITestCase

from app.models import GalleryImage


class GalleryListAPITest(APITestCase):
    url = "/api/gallery/"

    @classmethod
    def setUpTestData(cls):
        GalleryImage.objects.create(image="test-1.png", description="Gesichtsbehandlungen")
        GalleryImage.objects.create(image="test-2.png", description="Produkte")
        GalleryImage.objects.create(image="test-3.png", description="Körperbehandlungen")

    def test_list_return_200(self):
        response = self.client.get(self.url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_list_list_images(self):
        response = self.client.get(self.url)
        self.assertEqual(len(response.data), 3)

    def test_list_response_shape(self):
        response = self.client.get(self.url)
        self.assertIn("image", response.data[0])
        self.assertIn("description", response.data[0])


class GalleryListEmptyAPITest(APITestCase):
    url = "/api/gallery/"

    def test_list_empty_when_no_categories(self):
        GalleryImage.objects.all().delete()

        response = self.client.get(self.url)
        print("Response data:", response.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 0)
