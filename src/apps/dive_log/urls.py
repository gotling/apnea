from django.conf.urls import patterns, url

urlpatterns = patterns('',
    url(r'^$', 'dive_log.views.list_sessions', name='list_sessions'),
)
