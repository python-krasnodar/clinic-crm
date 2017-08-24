from django import forms


class AppointmentForm(forms.Form):
    speciality = forms.IntegerField()
    doctor = forms.IntegerField(required=True)
    day = forms.DateField(required=True)
    time = forms.TimeField(required=True)
    first_name = forms.CharField(required=True, max_length=128)
    last_name = forms.CharField(required=True, max_length=128)
