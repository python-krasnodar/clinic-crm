from rest_framework import serializers

from clinic.models import Doctor, Speciality


class SpecialitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Speciality
        fields = ('id', 'title')


class DoctorSerializer(serializers.ModelSerializer):
    speciality = SpecialitySerializer(many=False, read_only=True)

    class Meta:
        model = Doctor
        fields = ('id', 'first_name', 'last_name', 'speciality')

