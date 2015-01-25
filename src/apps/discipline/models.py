# coding=utf-8
from django.db import models
from django.utils.translation import ugettext as _


class Discipline(models.Model):
    abbreviation = models.CharField(_(u'Förkortning'), max_length=3)
    name = models.CharField(_(u'Namn'), max_length=64)

    def __unicode__(self):
        return u"{} - {}".format(self.abbreviation, self.name)