import datetime

from django.test import TestCase
from django.core.urlresolvers import resolve

from . import forms
from . import views
from . import models


class CreatePageTest(TestCase):

    def test_resolves_to_create_appointment_view(self):
        found = resolve('/')
        self.assertEqual(found.view_name, 'appointments:create')

    def test_create_page_uses_create_template(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'appointments/create.html')

    def test_create_page_contains_create_form(self):
        response = self.client.get('/')
        self.assertIsInstance(response.context_data['form'],
                            forms.AppointmentForm)

    def test_create_page_redirects_to_wright_url_after_POST(self):
        new_specialization = models.Specialization(name='Antropologist')
        new_specialization.save()

        new_doctor = models.Doctor(name='Johannus',
                                   second_name='Werter',
                                   specialization = new_specialization)

        new_doctor.save()
        data_list = {
            'patient_name': 'John',
            'patient_second_name': 'Donn',
            'patient_third_name': 'Ivanovich',
            'doctor': new_doctor.pk,
            'appointment_time':"2015-08-17 15:00",
            'specialization': new_specialization.pk
        }
        response = self.client.post('/', data=data_list, )
        new_appointment = models.Appointment.objects.first()
        self.assertRedirects(response,
                             new_appointment.get_absolute_url())
