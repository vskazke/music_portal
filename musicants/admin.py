from django.contrib import admin

from .models import *

class MusicantAdmin(admin.ModelAdmin):
    fieldsets = []

admin.site.register(Musicant, MusicantAdmin)

