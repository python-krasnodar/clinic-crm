from rest_framework import serializers

from clinic.models import Doctor, Speciality
from timetables.models import Timetable


class SpecialitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Speciality
        fields = ('id', 'title')


class DoctorSerializer(serializers.ModelSerializer):
    speciality = SpecialitySerializer(many=False, read_only=True)

    class Meta:
        model = Doctor
        fields = ('id', 'first_name', 'last_name', 'speciality')


class TimetableSerializer(serializers.ModelSerializer):
    class Meta:
        model = Timetable
        fields = ('id', 'doctor', 'day_of_week', 'start_time', 'end_time', 'break_start_time', 'break_end_time')
