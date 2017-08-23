from django.contrib import admin
from django.core.urlresolvers import reverse

from .models import Timetable


@admin.register(Timetable)
class TimetableAdmin(admin.ModelAdmin):
    list_display = ('day_of_week', 'doctor__url', 'start_time', 'end_time', 'break_start_time', 'break_end_time')
    list_filter = ('day_of_week', 'start_time', 'end_time', 'break_start_time', 'break_end_time')
    list_select_related = ('doctor',)
    search_fields = ('^doctor__first_name', '^doctor__last_name')
    fieldsets = (
        (None, {
            'fields': ('doctor',)
        }),
        ('Work Time', {
            'fields': ('day_of_week', 'start_time', 'end_time')
        }),
        ('Break Time', {
            'fields': ('break_start_time', 'break_end_time')
        })
    )

    def doctor__url(self, obj):
        url = reverse('admin:clinic_doctor_change', args=[obj.doctor.id])
        return '<a href="%s">%s</a>' % (url, obj.doctor)

    doctor__url.short_description = 'Doctor'
    doctor__url.admin_order_field = 'doctor__first_name'
    doctor__url.allow_tags = True
