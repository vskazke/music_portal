from django.contrib import admin

from .models import *


class Sing_inAdmin(admin.ModelAdmin):
    list_display = ('name', 'email')

admin.site.register(Sing_in, Sing_inAdmin)
admin.site.register(Login)
