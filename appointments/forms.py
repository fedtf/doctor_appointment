from django import forms
from django.utils.translation import ugettext as _

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit

from . import models

class AppointmentForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(AppointmentForm, self).__init__(*args, **kwargs)
        self.fields['doctor'].empty_label = _(u"Choose a doctor")
        self.fields['specialization'] = forms.ModelChoiceField(
                                            queryset=models.Specialization.objects.all())
        self.fields['specialization'].empty_label = _(u"Choose a specialization")
        self.fields['specialization'].label = _(u"Specialization")

        self.helper = FormHelper()
        self.helper.form_class = 'form-horizontal'
        self.helper.label_class = 'col-lg-2'
        self.helper.field_class = 'col-lg-8'
        self.helper.form_method = 'post'
        self.helper.form_action = '.'

        self.helper.add_input(Submit('submit', 'Submit'))

    def clean(self):
        """
        Raises ValidationError if chosen time is not available.
        """
        cleaned_data = super(AppointmentForm, self).clean()
        appointment_time = cleaned_data.get('appointment_time')
        if appointment_time:
            weekend = set([5, 6])

            if appointment_time.weekday() in weekend:
                raise forms.ValidationError(_('''Sorry, but we do not
                        work on the weekend.'''),  code='invalid')
            if appointment_time.hour >=18 or appointment_time.hour < 9:
                raise forms.ValidationError(_('''The working hours
                                        are 9-18'''),code='invalid')
            print(appointment_time)
            if appointment_time.minute != 0:
                raise forms.ValidationError(_('''The appointment can
                            start only in the beginning of an hour.'''),
                            code='invalid')


            doctor = cleaned_data.get('doctor')

            if doctor:
                if appointment_time in doctor.reserved_times:
                    raise forms.ValidationError(_('''This time is already
                                reserved, please choose another.'''),
                                code='invalid')

        return cleaned_data

    class Meta:
        model = models.Appointment
        fields = ('patient_name', 'patient_second_name',
                  'patient_third_name', 'doctor',
                  'appointment_time', 'complains')
        labels = {
            'patient_name': _(u'Name'),
            'patient_second_name': _(u'Second name'),
            'patient_third_name': _(u'Third name'),
            'doctor': _(u'Doctor'),
            'appointment_time': _(u'Appointment time'),
            'complains': _('Complains'),
        }
