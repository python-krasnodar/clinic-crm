from django.contrib import admin
from django.core.urlresolvers import reverse

from .models import Appointment


@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'doctor__url', 'appointment_day', 'start_time', 'end_time')
    fieldsets = (
        ('Customer', {
            'fields': ('first_name', 'last_name')
        }),
        ('Appointment', {
            'fields': ('doctor', 'appointment_day', 'start_time', 'end_time')
        })
    )

    def full_name(self, obj):
        return ' '.join([obj.first_name, obj.last_name])

    full_name.short_description = 'Customer'
    full_name.admin_order_field = 'first_name'

    def doctor__url(self, obj):
        url = reverse('admin:clinic_doctor_change', args=[obj.doctor.id])
        return '<a href="%s">%s</a>' % (url, obj.doctor)

    doctor__url.short_description = 'Doctor'
    doctor__url.admin_order_field = 'doctor__first_name'
    doctor__url.allow_tags = True