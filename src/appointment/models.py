from django.db import models


class Appointment(models.Model):
    first_name = models.CharField(max_length=128, blank=False, null=False)
    last_name = models.CharField(max_length=128, blank=False, null=False)
    appointment_day = models.DateField(blank=False, null=False)
    start_time = models.TimeField(blank=False, null=False)
    end_time = models.TimeField(blank=False, null=False)
    doctor = models.ForeignKey('clinic.Doctor', on_delete=models.CASCADE)

    def __str__(self):
        return '%s %s :: %s' % (self.first_name, self.last_name, self.doctor)

    class Meta:
        index_together = [
            ['first_name', 'last_name']
        ]
        unique_together = [
            ['doctor', 'appointment_day', 'start_time', 'end_time']
        ]
