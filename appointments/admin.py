from django.contrib import admin
from django.utils.translation import ugettext as _

from . import models


@admin.register(models.Appointment)
class AppointmentAdmin(admin.ModelAdmin):
    date_hierarchy = 'appointment_time'
    list_display = ('patient_second_name', 'patient_name',
                    'get_doctor', 'appointment_time',
                    'creation_time')

    def get_doctor(self, obj):
        return obj.doctor.second_name

    get_doctor.short_description = _(u"Doctor")
    get_doctor.admin_order_field = 'doctor'


@admin.register(models.Specialization)
class SpecializationAdmin(admin.ModelAdmin):
    list_display = ('name', 'get_doctors')

    def get_doctors(self, specialization):
        return obj.doctor_set

admin.site.register(models.Doctor)
