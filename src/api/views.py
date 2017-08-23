from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
from clinic.models import Doctor, Speciality
from timetables.models import Timetable
from .serializers import DoctorSerializer, SpecialitySerializer, TimetableSerializer


class DoctorViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer
    filter_backends = (DjangoFilterBackend,)
    filter_fields = ('speciality',)


class SpecialityViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Speciality.objects.all()
    serializer_class = SpecialitySerializer


class TimetableViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Timetable.objects.all()
    serializer_class = TimetableSerializer
    filter_backends = (DjangoFilterBackend,)
    filter_fields = ('doctor', 'day_of_week')
