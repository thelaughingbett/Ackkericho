from django.contrib import admin
from . import models 

# Register your models here.
admin.site.register(models.Event)
admin.site.register(models.Clergy)
admin.site.register(models.TodaysDate)
admin.site.register(models.Gallery)