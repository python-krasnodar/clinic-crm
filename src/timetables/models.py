from django.db import models


class Timetable(models.Model):
    DW_MON = 0
    DW_TUE = 1
    DW_WED = 2
    DW_THU = 3
    DW_FRI = 4

    DAY_OF_WEEK_CHOICES = (
        (DW_MON, 'Monday'),
        (DW_TUE, 'Tuesday'),
        (DW_WED, 'Wednesday'),
        (DW_THU, 'Thursday'),
        (DW_FRI, 'Friday'),
    )

    day_of_week = models.IntegerField(choices=DAY_OF_WEEK_CHOICES, null=False, blank=False)
    start_time = models.TimeField(null=False, blank=False)
    end_time = models.TimeField(null=False, blank=False)
    break_start_time = models.TimeField(null=False, blank=False)
    break_end_time = models.TimeField(null=False, blank=False)
    doctor = models.ForeignKey('clinic.Doctor', on_delete=models.CASCADE)

    def __str__(self):
        return 'Timetable for "%s" %s %s-%s (%s-%s)' % (
            str(self.doctor),
            dict(Timetable.DAY_OF_WEEK_CHOICES)[self.day_of_week],
            self.start_time,
            self.end_time,
            self.break_start_time,
            self.break_end_time,
        )

    class Meta:
        unique_together = [
            ['doctor', 'day_of_week'],
        ]
