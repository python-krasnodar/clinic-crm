from django.test import TestCase
from .models import Doctor, Speciality


class SpecialityStrTestCase(TestCase):
    TITLE = 'test'

    def setUp(self):
        Speciality.objects.create(title=SpecialityStrTestCase.TITLE)

    def test_speciality_str_representation_return_title(self):
        spec = Speciality.objects.get(title=SpecialityStrTestCase.TITLE)

        self.assertEqual(str(spec), SpecialityStrTestCase.TITLE)


class SpecialityDefaultOrderTestCase(TestCase):
    def setUp(self):
        Speciality.objects.create(title='One', sorder=10)
        Speciality.objects.create(title='Two', sorder=20)
        Speciality.objects.create(title='Zero', sorder=0)

    def test_default_order_is_sorder(self):
        specs = Speciality.objects.all()

        self.assertEqual(specs[0].title, 'Zero')
        self.assertEqual(specs[1].title, 'One')
        self.assertEqual(specs[2].title, 'Two')


class DoctorStrTestCase(TestCase):
    FIRST_NAME = 'John'
    LAST_NAME = 'Doe'

    def setUp(self):
        spec = Speciality.objects.create(title='test')

        Doctor.objects.create(first_name=DoctorStrTestCase.FIRST_NAME,
                              last_name=DoctorStrTestCase.LAST_NAME,
                              speciality=spec)

    def test_doctor_str_representation_return_full_name(self):
        doctor = Doctor.objects.get(first_name=DoctorStrTestCase.FIRST_NAME,
                                         last_name=DoctorStrTestCase.LAST_NAME)

        self.assertEqual(str(doctor), ' '.join([DoctorStrTestCase.FIRST_NAME, DoctorStrTestCase.LAST_NAME]))


class DoctorDefaultOrderTestCase(TestCase):
    def setUp(self):
        spec = Speciality.objects.create(title='Test')

        Doctor.objects.create(first_name='Doctor', last_name='One', speciality=spec, sorder=10)
        Doctor.objects.create(first_name='Doctor', last_name='Two', speciality=spec, sorder=20)
        Doctor.objects.create(first_name='Doctor', last_name='Zero', speciality=spec, sorder=0)

    def test_default_order_is_sorder(self):
        doctors = Doctor.objects.all()

        self.assertEqual(doctors[0].last_name, 'Zero')
        self.assertEqual(doctors[1].last_name, 'One')
        self.assertEqual(doctors[2].last_name, 'Two')
