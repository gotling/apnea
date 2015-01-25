from django.contrib import admin
from discipline.models import Discipline


class DisciplineAdmin(admin.ModelAdmin):
    ordering = ['abbreviation']


admin.site.register(Discipline, DisciplineAdmin)