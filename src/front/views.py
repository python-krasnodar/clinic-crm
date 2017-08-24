import datetime

from django.core.urlresolvers import reverse
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect

from .forms import AppointmentForm
from appointment.models import Appointment


def index(request):
    if request.method == 'POST':
        form = AppointmentForm(request.POST)

        if form.is_valid():
            start_time = datetime.datetime.strptime(form.data['time'], '%H:%M')
            end_time = start_time + datetime.timedelta(hours=1)

            appointment = Appointment()
            appointment.doctor_id = form.data['doctor']
            appointment.appointment_day = form.data['day']
            appointment.start_time = start_time.strftime('%H:%M')
            appointment.end_time = end_time.strftime('%H:%M')
            appointment.first_name = form.data['first_name']
            appointment.last_name = form.data['last_name']
            appointment.save()

            return HttpResponseRedirect(reverse('front:details', args=[appointment.id]))
    else:
        form = AppointmentForm()

    return render(request, 'front/index.html', {'form': form})


def details(request, pk):
    appointment = get_object_or_404(Appointment, pk=pk)

    return render(request, 'front/details.html', {
        'appointment': appointment,
    })
