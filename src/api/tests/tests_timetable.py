import datetime

from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from clinic.models import Doctor, Speciality
from timetables.models import Timetable


class TimetableTestCase(APITestCase):
    def test_return_empty_list(self):
        response = self._get_response()

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, [])

    def test_return_not_empty_list(self):
        spec = Speciality.objects.create(title='Test')
        doc = Doctor.objects.create(speciality=spec, first_name='Doctor', last_name='Test')

        Timetable.objects.create(doctor=doc,
                                 day_of_week=Timetable.DW_MON,
                                 start_time=datetime.time(hour=8),
                                 end_time=datetime.time(hour=17),
                                 break_start_time=datetime.time(hour=12),
                                 break_end_time=datetime.time(hour=13))
        Timetable.objects.create(doctor=doc,
                                 day_of_week=Timetable.DW_TUE,
                                 start_time=datetime.time(hour=9),
                                 end_time=datetime.time(hour=18),
                                 break_start_time=datetime.time(hour=12),
                                 break_end_time=datetime.time(hour=13))

        response = self._get_response()

        self.assertEqual(len(response.data), Timetable.objects.count())

    def test_return_correcct_list(self):
        spec = Speciality.objects.create(title='Test')
        doc = Doctor.objects.create(speciality=spec, first_name='Doctor', last_name='Test')

        tt = Timetable.objects.create(doctor=doc,
                                      day_of_week=Timetable.DW_MON,
                                      start_time=datetime.time(hour=8),
                                      end_time=datetime.time(hour=17),
                                      break_start_time=datetime.time(hour=12),
                                      break_end_time=datetime.time(hour=13))

        response = self._get_response()

        tf = '%H:%M:%S'

        self.assertEqual(response.data[0]['doctor'], doc.id)
        self.assertEqual(response.data[0]['day_of_week'], tt.day_of_week)
        self.assertEqual(response.data[0]['start_time'], tt.start_time.strftime(tf))
        self.assertEqual(response.data[0]['end_time'], tt.end_time.strftime(tf))
        self.assertEqual(response.data[0]['break_start_time'], tt.break_start_time.strftime(tf))
        self.assertEqual(response.data[0]['break_end_time'], tt.break_end_time.strftime(tf))

    def test_filter_by_doctor(self):
        spec = Speciality.objects.create(title='Test')
        doc1 = Doctor.objects.create(speciality=spec, first_name='Doctor', last_name='One')
        doc2 = Doctor.objects.create(speciality=spec, first_name='Doctor', last_name='Two')

        Timetable.objects.create(doctor=doc1,
                                 day_of_week=Timetable.DW_MON,
                                 start_time=datetime.time(hour=8),
                                 end_time=datetime.time(hour=17),
                                 break_start_time=datetime.time(hour=12),
                                 break_end_time=datetime.time(hour=13))
        Timetable.objects.create(doctor=doc1,
                                 day_of_week=Timetable.DW_TUE,
                                 start_time=datetime.time(hour=9),
                                 end_time=datetime.time(hour=18),
                                 break_start_time=datetime.time(hour=12),
                                 break_end_time=datetime.time(hour=13))
        Timetable.objects.create(doctor=doc2,
                                 day_of_week=Timetable.DW_MON,
                                 start_time=datetime.time(hour=8),
                                 end_time=datetime.time(hour=17),
                                 break_start_time=datetime.time(hour=12),
                                 break_end_time=datetime.time(hour=13))

        response = self._get_response(doctor=doc1.id)

        self.assertEqual(len(response.data), doc1.timetable_set.count())

    def test_filter_by_day_of_week(self):
        spec = Speciality.objects.create(title='Test')
        doc1 = Doctor.objects.create(speciality=spec, first_name='Doctor', last_name='One')
        doc2 = Doctor.objects.create(speciality=spec, first_name='Doctor', last_name='Two')

        Timetable.objects.create(doctor=doc1,
                                 day_of_week=Timetable.DW_MON,
                                 start_time=datetime.time(hour=8),
                                 end_time=datetime.time(hour=17),
                                 break_start_time=datetime.time(hour=12),
                                 break_end_time=datetime.time(hour=13))
        Timetable.objects.create(doctor=doc1,
                                 day_of_week=Timetable.DW_TUE,
                                 start_time=datetime.time(hour=9),
                                 end_time=datetime.time(hour=18),
                                 break_start_time=datetime.time(hour=12),
                                 break_end_time=datetime.time(hour=13))
        Timetable.objects.create(doctor=doc2,
                                 day_of_week=Timetable.DW_MON,
                                 start_time=datetime.time(hour=8),
                                 end_time=datetime.time(hour=17),
                                 break_start_time=datetime.time(hour=12),
                                 break_end_time=datetime.time(hour=13))

        response = self._get_response(day_of_week=Timetable.DW_MON)

        self.assertEqual(len(response.data), Timetable.objects.filter(day_of_week=Timetable.DW_MON).count())

    def _get_response(self, **kwargs):
        url = reverse('api:timetable-list')
        return self.client.get(url, data=kwargs, format='json')


