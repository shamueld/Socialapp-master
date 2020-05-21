from django.contrib import admin

from . import models

# Register your models here. 

admin.site.register(models.Server)
admin.site.register(models.EAI)
admin.site.register(models.Application)
