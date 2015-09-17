from django.conf.urls import url

from . import views


urlpatterns = [
    url(r'^$', views.CreateAppointmentView.as_view(), name="create"),
    url(r'^(?P<pk>[0-9]+)/$', views.DetailAppointmentView.as_view(),
                                                      name="detail")
]
