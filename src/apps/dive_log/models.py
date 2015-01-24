# coding=utf-8
from django.db import models
from django.utils.translation import ugettext as _
#from taggit.managers import TaggableManager


class Session(models.Model):
    date = models.DateField(verbose_name=_(u'Datum'))
    time = models.TimeField(verbose_name=_(u'Tid'))
    comment = models.CharField(verbose_name=_(u'Kommentar'), max_length=512)

    class Meta:
        verbose_name = _(u'Session')
        verbose_name_plural = _(u'Sessioner')
        ordering = ['date', 'time']

    def __unicode__(self):
        return self.date


class Dive(models.Model):
    session = models.ForeignKey(Session)
    #discipline = models.ForeignKey(Discipline)
    start = models.TimeField()
    stop = models.TimeField(verbose_name=_(u'Stopp'))
    distance = models.IntegerField(verbose_name=_(u'Längd'), default=0)
    temperature = models.IntegerField(verbose_name=_(u'Temperatur'))
    comment = models.CharField(verbose_name=_(u'Kommentar'), max_length=512)
    #tags = TaggableManager()

    class Meta:
        verbose_name = _(u'Dyk')
        verbose_name_plural = _(u'Dyk')

    def __unicode__(self):
        return {}.format(self.distance)