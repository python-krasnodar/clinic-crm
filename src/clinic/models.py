from django.db import models


class Speciality(models.Model):
    title = models.CharField(max_length=128, blank=False, null=False, unique=True)
    sorder = models.IntegerField(blank=True, null=False, default=0)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['sorder']


class Doctor(models.Model):
    first_name = models.CharField(max_length=128, blank=False, null=False)
    last_name = models.CharField(max_length=128, blank=False, null=False)
    sorder = models.IntegerField(blank=True, null=False, default=0)
    speciality = models.ForeignKey(Speciality, on_delete=models.PROTECT)

    def __str__(self):
        return ' '.join([self.first_name, self.last_name])

    class Meta:
        ordering = ['sorder']
