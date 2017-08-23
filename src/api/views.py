import datetime
from rest_framework import viewsets, status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend

from appointment.models import Appointment
from clinic.models import Doctor, Speciality
from timetables.models import Timetable
from .serializers import AppointmentSerializer, DoctorSerializer, SpecialitySerializer, TimetableSerializer


@api_view(['GET', 'HEAD'])
def get_times(request, doctor_id, day, format=None):
    try:
        doctor = Doctor.objects.get(pk=doctor_id)
    except Doctor.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    dt = datetime.datetime.strptime(day, '%Y-%m-%d')
    weekday = dt.weekday()

    try:
        timetable = doctor.timetable_set.get(day_of_week=weekday)
    except Timetable.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    appointments = doctor.appointment_set.filter(appointment_day=day)
    busy_hours = [app.start_time.hour for app in appointments]
    busy_hours.append(timetable.break_start_time.hour)

    hours = [datetime.time(hour=h, minute=timetable.start_time.minute).strftime('%H:%M') for h in range(timetable.start_time.hour, timetable.end_time.hour) if h not in busy_hours]

    return Response(hours)


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
