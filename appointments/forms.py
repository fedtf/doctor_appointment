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
        self.helper = FormHelper()
        self.helper.form_class = 'form-horizontal'
        self.helper.label_class = 'col-lg-2'
        self.helper.field_class = 'col-lg-8'
        self.helper.form_method = 'post'
        self.helper.form_action = '.'

        self.helper.add_input(Submit('submit', 'Submit'))

    def clean(self):
        cleaned_data = super(AppointmentForm, self).clean()
        appointment_time = cleaned_data['appointment_time']

        weekend = set([5, 6])
        if appointment_time.weekday() in weekend:
            raise forms.ValidationError(_('Sorry, but we are not working on weekends'),
                                        code='invalid')

        doctor = cleaned_data['doctor']

        if appointment_time in doctor.reserved_times:
            raise forms.ValidationError(_('This time is already reserved, please choose another'),
                                        code='invalid')

        return cleaned_data

    class Meta:
        model = models.Appointment
        exclude = ('creation_time',)