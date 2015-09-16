from django.shortcuts import render
from django.views.generic.edit import CreateView
from django.utils.translation import ugettext_lazy as _
from django.core.urlresolvers import reverse_lazy

from braces.views import FormMessagesMixin

from . import forms
from . import models

class CreateAppointmentView(FormMessagesMixin, CreateView):
    form_class = forms.AppointmentForm
    template_name = 'appointments/create.html'
    form_valid_message = _(u"Appointment successfully created.")
    form_invalid_message = _(u"Something went wrong, check errors below.")
    success_url = reverse_lazy('appointments:create')

    def get_context_data(self, **kwargs):
        context_data = super(CreateAppointmentView, self).get_context_data(**kwargs)
        context_data['doctors'] = models.Doctor.objects.all()
        context_data['specializations'] = models.Specialization.objects.all()

        return context_data
