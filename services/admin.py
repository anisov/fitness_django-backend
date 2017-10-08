from django.contrib import admin
from .models import *
# Register your models here.


class ServicesAdmin(admin.ModelAdmin):
    verbose_name = "Услуги"


admin.site.register(ServicesModel, ServicesAdmin)
