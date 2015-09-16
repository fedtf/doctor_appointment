from django.conf.urls import url

from . import views


urlpatterns = [
    url(r'^$', views.CreateAppointmentView.as_view(), name="create"),
]
