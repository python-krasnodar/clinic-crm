from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from clinic.models import Doctor, Speciality


class DoctorTestCase(APITestCase):
    def test_return_empty_list(self):
        response = self._get_response()

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, [])

    def test_return_not_empty_list(self):
        spec = Speciality.objects.create(title='Test')

        Doctor.objects.create(speciality=spec, first_name='Doctor', last_name='One')
        Doctor.objects.create(speciality=spec, first_name='Doctor', last_name='Two')

        response = self._get_response()

        self.assertEqual(len(response.data), Doctor.objects.count())

    def test_return_correct_list(self):
        spec = Speciality.objects.create(title='Test')

        doc = Doctor.objects.create(speciality=spec, first_name='Doctor', last_name='Test')

        response = self._get_response()

        self.assertEqual(response.data[0]['first_name'], doc.first_name)
        self.assertEqual(response.data[0]['last_name'], doc.last_name)

    def test_filter_by_speciality(self):
        spec1 = Speciality.objects.create(title='One')
        spec2 = Speciality.objects.create(title='Two')

        Doctor.objects.create(speciality=spec1, first_name='Doctor', last_name='One')
        Doctor.objects.create(speciality=spec1, first_name='Doctor', last_name='Two')
        Doctor.objects.create(speciality=spec1, first_name='Doctor', last_name='Three')
        Doctor.objects.create(speciality=spec2, first_name='Doctor', last_name='One')
        Doctor.objects.create(speciality=spec2, first_name='Doctor', last_name='Two')

        response = self._get_response(speciality=spec1.id)

        self.assertEqual(len(response.data), spec1.doctor_set.count())

    def _get_response(self, **kwargs):
        url = reverse('api:doctor-list')
        return self.client.get(url, data=kwargs, format='json')