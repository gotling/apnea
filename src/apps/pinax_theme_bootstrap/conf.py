from django.conf import settings  # noqa

from appconf import AppConf


class ThemeAppConf(AppConf):

    ADMIN_URL = "admin:index"
    CONTACT_EMAIL = "support@apnea.gosy.se"
    SITE_NAME = "Apnea"

    class Meta:
        prefix = "theme"
