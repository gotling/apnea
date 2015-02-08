# coding=utf-8
from django.contrib.auth.models import User
from django.db import models
from django.utils.translation import ugettext as _
from discipline.models import Discipline


class Session(models.Model):
    #pool = models.ForeignKey(Pool)
    user = models.ForeignKey(User)
    date = models.DateField(verbose_name=_(u'Datum'))
    time = models.TimeField(verbose_name=_(u'Tid'))
    comment = models.CharField(verbose_name=_(u'Kommentar'), max_length=512, blank=True)

    class Meta:
        verbose_name = _(u'Session')
        verbose_name_plural = _(u'Sessioner')
        ordering = ['date', 'time']

    def __unicode__(self):
        return "{} {}".format(self.date, self.time)


class Dive(models.Model):
    session = models.ForeignKey(Session)
    discipline = models.ForeignKey(Discipline, verbose_name=_(u'Disciplin'), null=True, blank=True)
    rest_duration = models.DurationField(_(u'Vila'), null=True, blank=True)
    start = models.TimeField(null=True, blank=True)
    dive_duration = models.DurationField(_(u'Dyktid'), null=True, blank=True)
    distance = models.IntegerField(_(u'Distans'), help_text=_(u'i meter'), null=True)
    temperature = models.IntegerField(_(u'Temperatur'), help_text=_(u'i celsius'), null=True, blank=True)
    comment = models.CharField(_(u'Kommentar'), max_length=512, blank=True)
    # TODO: Tag migrations broken with Django 1.7.2 https://github.com/alex/django-taggit/issues/285
    #tags = TaggableManager(verbose_name=_(u'Taggar'), blank=True)

    class Meta:
        verbose_name = _(u'Dyk')
        verbose_name_plural = _(u'Dyk')
        ordering = ['id']

    def __unicode__(self):
        if self.discipline:
            return "{} - {}".format(self.discipline.abbreviation, str(self.dive_duration))
        else:
            return str(self.dive_duration)


class DataPoint(models.Model):
    dive = models.ForeignKey(Dive)
    second = models.IntegerField(verbose_name=_(u'Sekund'))
    depth = models.DecimalField(verbose_name=_(u'Djup'), decimal_places=1, max_digits=4, null=True, blank=True)
    temperature = models.DecimalField(verbose_name=_(u'Temperatur'), decimal_places=1, max_digits=3, null=True, blank=True)
    heart_rate = models.IntegerField(verbose_name=_(u'Puls'), null=True, blank=True)

    class Meta:
        verbose_name = _(u'Datapunkt')
        verbose_name_plural = _(u'Datapunkter')
        ordering = ['second']

    def __unicode__(self):
        return u'{} - {} m'.format(self.second, self.depth)