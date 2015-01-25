# coding=utf-8
from django.db import models
from django.utils.translation import ugettext as _

class Session(models.Model):
    #pool = models.ForeignKey(Pool)
    date = models.DateField(verbose_name=_(u'Datum'))
    time = models.TimeField(verbose_name=_(u'Tid'))
    comment = models.CharField(verbose_name=_(u'Kommentar'), max_length=512, blank=True)

    class Meta:
        verbose_name = _(u'Session')
        verbose_name_plural = _(u'Sessioner')
        ordering = ['date', 'time']

    def __unicode__(self):
        return "{}".format(self.date)


class Dive(models.Model):
    session = models.ForeignKey(Session)
    #discipline = models.ForeignKey(Discipline)
    start = models.TimeField(null=True, blank=True)
    rest_duration = models.IntegerField(_(u'Vila innan'), help_text=_(u'Sekunder'), null=True)
    dive_duration = models.IntegerField(_(u'Dyktid'), help_text=_(u'Sekunder'), null=True, blank=True)
    distance = models.IntegerField(verbose_name=_(u'Distans'), null=True)
    temperature = models.IntegerField(verbose_name=_(u'Temperatur'), null=True, blank=True)
    comment = models.CharField(verbose_name=_(u'Kommentar'), max_length=512, blank=True)
    # TODO: Tag migrations broken with Django 1.7.2 https://github.com/alex/django-taggit/issues/285
    #tags = TaggableManager(verbose_name=_(u'Taggar'), blank=True)

    class Meta:
        verbose_name = _(u'Dyk')
        verbose_name_plural = _(u'Dyk')

    def __unicode__(self):
        return "{}".format(self.distance)