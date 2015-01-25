from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _


class DiveLogConfig(AppConfig):
    name = 'dive_log'
    verbose_name = _(u'Dyklog')