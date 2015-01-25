from django.contrib import admin
from django.utils.translation import ugettext as _
from .models import Session, Dive


class DiveInline(admin.TabularInline):
    model = Dive


class SessionAdmin(admin.ModelAdmin):
    list_display = ('__unicode__', 'dive_count', 'comment')
    list_filter = ('date',)

    inlines = [DiveInline]

    def dive_count(self, obj):
        return obj.dive_set.count()
    dive_count.short_description = _(u'Antal dyk')


class DiveAdmin(admin.ModelAdmin):
    list_display = ('session', )


admin.site.register(Session, SessionAdmin)
admin.site.register(Dive, DiveAdmin)

