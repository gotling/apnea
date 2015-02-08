from django.conf.urls import patterns, include, url
from django.contrib import admin

from dive_log import urls as dive_log_urls
from uploader import urls as uploader_urls
from views import home


urlpatterns = patterns('',
    # Home
    url(r'^$', home, name='home'),

    # Dive log
    url(r'^/?', include(dive_log_urls)),

    # Upload
    url(r'^upload/?', include(uploader_urls)),

    # Accounts
    url(r"^account/", include("account.urls")),

    # Admin
    url(r'^admin/', include(admin.site.urls)),
)
