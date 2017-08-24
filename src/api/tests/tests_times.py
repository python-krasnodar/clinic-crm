import datetime

from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from clinic.models import Doctor, Speciality
from timetables.models import Timetable
from appointment.models import Appointment


class TimesTestCase(APITestCase):
    def test_return_404(self):
        response = self._get_response(doctor_id=1, day='2017-10-10')

        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_return_hours(self):
        spec = Speciality.objects.create(title='Test')
        doc = Doctor.objects.create(speciality=spec, first_name='Doctor', last_name='Test')

        tt = Timetable.objects.create(doctor=doc,
                                      day_of_week=Timetable.DW_MON,
                                      start_time=datetime.time(hour=8),
                                      end_time=datetime.time(hour=17),
                                      break_start_time=datetime.time(hour=12),
                                      break_end_time=datetime.time(hour=13))

        response = self._get_response(doctor_id=doc.id, day='2017-08-14')

        break_time = tt.break_end_time.hour - tt.break_start_time.hour
        work_time = tt.end_time.hour - tt.start_time.hour

        self.assertEqual(len(response.data), work_time - break_time)

    def _get_response(self, **kwargs):
        url = reverse('api:get-times', kwargs=kwargs)
        return self.client.get(url, format='json')