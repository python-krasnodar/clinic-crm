import datetime

from django.test import TestCase

from clinic.models import Doctor, Speciality
from .models import Timetable


class TimetableStrTestCase(TestCase):
    def setUp(self):
        spec = Speciality.objects.create(title='Test')
        doctor = Doctor.objects.create(first_name='Doctor', last_name='Test', speciality=spec)

        Timetable.objects.create(doctor=doctor,
                                 day_of_week=Timetable.DW_MON,
                                 start_time=datetime.time(hour=8),
                                 end_time=datetime.time(hour=17),
                                 break_start_time=datetime.time(hour=12),
                                 break_end_time=datetime.time(hour=13))

    def test_timetable_str_representation_format(self):
        timetable = Timetable.objects.get(day_of_week=Timetable.DW_MON)

        self.assertEqual(str(timetable),
                         'Timetable for "%s" %s %s-%s (%s-%s)' % (
                             timetable.doctor,
                             dict(Timetable.DAY_OF_WEEK_CHOICES)[timetable.day_of_week],
                             timetable.start_time,
                             timetable.end_time,
                             timetable.break_start_time,
                             timetable.break_end_time
                         ))
