from django.conf.urls import patterns, include, url
from django.contrib import admin

from dive_log import urls as dive_log_urls
from uploader import urls as uploader_urls


urlpatterns = patterns('',
    # Dive log
    url(r'^/?', include(dive_log_urls), name='home'),

    # Upload
    url(r'^upload/?', include(uploader_urls)),

    # Accounts
    url(r"^account/", include("account.urls")),

    # Admin
    url(r'^admin/', include(admin.site.urls)),
)
