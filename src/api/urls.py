from django.conf.urls import url, include
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'doctors', views.DoctorViewSet)
router.register(r'specialities', views.SpecialityViewSet)
router.register(r'timetables', views.TimetableViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^times/(?P<doctor_id>[0-9]+)/(?P<day>\d{4}\-\d{2}\-\d{2})/$', views.get_times, name='get-times'),
    url(r'^auth/', include('rest_framework.urls', namespace='rest_framework')),
]
