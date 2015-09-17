from django.shortcuts import render
from django.views.generic.edit import CreateView
from django.views.generic.detail import DetailView
from django.utils.translation import ugettext_lazy as _
from django.core.urlresolvers import reverse_lazy

from braces.views import FormValidMessageMixin

from . import forms
from . import models

class CreateAppointmentView(FormValidMessageMixin, CreateView):
    form_class = forms.AppointmentForm
    template_name = 'appointments/create.html'
    form_valid_message = _(u"Appointment successfully created.")

    def get_context_data(self, **kwargs):
        context_data = super(CreateAppointmentView, self).get_context_data(**kwargs)

        #probably query overhead
        context_data['doctors'] = models.Doctor.objects.all()
        context_data['specializations'] = models.Specialization.objects.all()

        return context_data


class DetailAppointmentView(DetailView):
    model = models.Appointment
    template_name = 'appointments/detail.html'
