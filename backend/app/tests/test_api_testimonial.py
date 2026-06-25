from rest_framework import status
from rest_framework.test import APITestCase

from app.models import Testimonial


class TestimonialListAPITest(APITestCase):
    url = "/api/testimonial/"

    @classmethod
    def setUpTestData(cls):
        for index in range(8):
            Testimonial.objects.create(
                first_name=f"Vor{index}",
                last_name=f"Nach{index}",
                text=f"Bewertung {index}",
                rating=5,
            )

    def test_list_return_200(self):
        response = self.client.get(self.url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_list_returns_at_most_six_random_testimonials(self):
        response = self.client.get(self.url)

        self.assertEqual(len(response.data), 6)

    def test_list_response_shape(self):
        response = self.client.get(self.url)
        item = response.data[0]

        self.assertIn("first_name", item)
        self.assertIn("last_name", item)
        self.assertIn("full_name", item)
        self.assertIn("text", item)
        self.assertIn("rating", item)

    def test_get_user_full_name(self):
        response = self.client.get(self.url)
        data = response.data[0]

        self.assertEqual(data["full_name"], f"{data['first_name']} {data['last_name']}")


class TestimonialListEmptyAPITest(APITestCase):
    url = "/api/testimonial/"

    def test_list_empty_when_no_testimonials(self):
        Testimonial.objects.all().delete()

        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 0)


class TestimonialListSmallSampleAPITest(APITestCase):
    url = "/api/testimonial/"

    @classmethod
    def setUpTestData(cls):
        Testimonial.objects.create(
            first_name="Max", last_name="Muster", text="Top!", rating=5
        )
        Testimonial.objects.create(
            first_name="Anna",
            last_name="Beispiel",
            text="Sehr gut!",
            rating=5,
        )

    def test_list_returns_all_when_fewer_than_sample_size(self):
        response = self.client.get(self.url)

        self.assertEqual(len(response.data), 2)
