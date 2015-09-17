from django.shortcuts import render
from django.views.generic.edit import CreateView
from django.views.generic.detail import DetailView
from django.utils.translation import ugettext_lazy as _
from django.core.urlresolvers import reverse_lazy

from braces.views import FormMessagesMixin, UserPassesTestMixin

from . import forms
from . import models

class CreateAppointmentView(FormMessagesMixin, CreateView):
    form_class = forms.AppointmentForm
    template_name = 'appointments/create.html'
    form_valid_message = _(u"Appointment successfully created.")
    form_invalid_message = _(u"Something went wrong, check errors below.")

    def get_success_url(self):
        return '{}?hash={}'.format(self.object.get_absolute_url(),
                            self.request.user.get_session_auth_hash())

    def get_context_data(self, **kwargs):
        context_data = super(CreateAppointmentView, self).get_context_data(**kwargs)

        #probably query overhead
        context_data['doctors'] = models.Doctor.objects.all()
        context_data['specializations'] = models.Specialization.objects.all()

        return context_data


class DetailAppointmentView(UserPassesTestMixin, DetailView):
    model = models.Appointment
    template_name = 'appointments/detail.html'
    raise_exception = True

    def test_func(self, user):
        return self.request.GET.get('hash', False) == user.get_session_auth_hash()
