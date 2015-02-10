from django.conf.urls import patterns, url
from .views import details, upload

urlpatterns = patterns('',
    url(r'^details/(?P<dive_id>\d+)$', details, name='details'),
    url(r'^upload/?', upload, name='upload'),
    url(r'^(?P<username>\w+)$', 'dive_log.views.list_sessions', name='list_sessions'),
)
