from django.conf.urls import url, include
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'doctors', views.DoctorViewSet)
router.register(r'specialities', views.SpecialityViewSet)
router.register(r'timetables', views.TimetableViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^auth/', include('rest_framework.urls', namespace='rest_framework')),
]
