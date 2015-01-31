from django.conf.urls import patterns, url
from .views import details

urlpatterns = patterns('',
    url(r'^$', 'dive_log.views.list_sessions', name='list_sessions'),
    url(r'^details/(?P<dive_id>\d+)$', details, name='details'),
)
