from django.contrib import admin
from .models import Session, Dive


class DiveInline(admin.TabularInline):
    model = Dive


class SessionAdmin(admin.ModelAdmin):
    list_display = ('date', 'comment')
    list_filter = ('date',)

    inlines = [DiveInline]


class DiveAdmin(admin.ModelAdmin):
    list_display = ('session', )


admin.site.register(Session, SessionAdmin)
admin.site.register(Dive, DiveAdmin)

