from django.contrib import admin
from django.core.urlresolvers import reverse

from .models import Doctor, Speciality


@admin.register(Speciality)
class SpecialityAdmin(admin.ModelAdmin):
    search_fields = ('^title',)
    fieldsets = (
        (None, {
            'fields': ('title',)
        }),
        ('Optional', {
            'classes': ('collapse',),
            'fields': ('sorder',)
        })
    )


@admin.register(Doctor)
class DoctorAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'speciality__url')
    list_filter = ('speciality',)
    list_select_related = ('speciality',)
    search_fields = ('^first_name', '^last_name')
    fieldsets = (
        (None, {
            'fields': ('speciality',)
        }),
        (None, {
            'fields': ('first_name', 'last_name')
        }),
        ('Optional', {
            'classes': ('collapse',),
            'fields': ('sorder',)
        })
    )

    def full_name(self, obj):
        return obj.__str__()

    full_name.short_description = 'Full Name'
    full_name.admin_order_field = 'first_name'

    def speciality__url(self, obj):
        url = reverse('admin:clinic_speciality_change', args=[obj.speciality.id])
        return '<a href="%s">%s</a>' % (url, obj.speciality.title)

    speciality__url.short_description = 'Speciality'
    speciality__url.admin_order_field = 'speciality__title'
    speciality__url.allow_tags = True
