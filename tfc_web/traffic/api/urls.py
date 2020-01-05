from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^zone/$', views.ZoneList.as_view()),
    url(r'^zone/(?P<zone_id>[^/]+)/$', views.ZoneConfig.as_view()),
    url(r'^zone/history/(?P<zone_id>[^/]+)/$', views.ZoneHistory.as_view()),
    url(r'^anpr/camera/$', views.ANPRCameraList.as_view()),
    url(r'^anpr/trip/$', views.ANPRTripList.as_view()),
]
