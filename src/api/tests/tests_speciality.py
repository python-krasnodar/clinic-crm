from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from clinic.models import Speciality


class SpecialityTestCase(APITestCase):
    def test_return_empty_list(self):
        response = self._get_response()

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, [])

    def test_return_not_empty_list(self):
        Speciality.objects.create(title='Test One')
        Speciality.objects.create(title='Test Two')

        response = self._get_response()

        self.assertEqual(len(response.data), Speciality.objects.count())

    def test_return_correct_list(self):
        spec = Speciality.objects.create(title='Test One')

        response = self._get_response()

        self.assertEqual(response.data[0]['title'], spec.title)

    def _get_response(self):
        url = reverse('api:speciality-list')
        return self.client.get(url, format='json')