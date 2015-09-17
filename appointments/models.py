from django.db import models
from django.core.urlresolvers import reverse
from django.utils.translation import ugettext_lazy as _


class Specialization(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Doctor(models.Model):
    name = models.CharField(max_length=50)
    second_name = models.CharField(max_length=50)
    specialization = models.ForeignKey(Specialization)

    def __str__(self):
        return (_('Dr. ') + '{}. {}').format(self.name[0],
                                             self.second_name)

    @property
    def reserved_times(self):
        return set(dt.appointment_time for dt in self.appointment_set.all())


class Appointment(models.Model):
    patient_name = models.CharField(max_length=50)
    patient_second_name = models.CharField(max_length=50)
    patient_third_name = models.CharField(max_length=50)
    creation_time = models.DateTimeField(auto_now_add=True)
    doctor = models.ForeignKey(Doctor)
    appointment_time = models.DateTimeField()
    complains = models.TextField(blank=True)

    def __str__(self):
        return '{} {} {}'.format(self.patient_second_name, self.doctor,
                         self.appointment_time.strftime('%m-%d %H:%M'))

    def get_absolute_url(self):
        return reverse('appointments:detail', kwargs={'pk':self.pk})
