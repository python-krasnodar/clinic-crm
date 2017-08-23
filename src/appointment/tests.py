import datetime
from django.test import TestCase

from clinic.models import Doctor, Speciality
from .models import Appointment


class AppointmentStrTestCase(TestCase):
    FIRST_NAME = 'Customer'
    LAST_NAME = 'Test'

    def setUp(self):
        spec = Speciality.objects.create(title='Test')
        doc = Doctor.objects.create(first_name='Doctor', last_name='Test', speciality=spec)

        Appointment.objects.create(doctor=doc,
                                   first_name=AppointmentStrTestCase.FIRST_NAME,
                                   last_name=AppointmentStrTestCase.LAST_NAME,
                                   appointment_day=datetime.date(year=2017, month=8, day=10),
                                   start_time=datetime.time(hour=8),
                                   end_time=datetime.time(hour=9))

    def test_appointment_str_representation_return_customer_and_doctor(self):
        a = Appointment.objects.get(doctor__first_name='Doctor', doctor__last_name='Test')
        doc = a.doctor
        full_name = ' '.join([a.first_name, a.last_name])

        self.assertEqual(str(a), ' :: '.join([full_name, str(doc)]))