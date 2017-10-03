from django.contrib import admin
from .models import *
class Comments_admin(admin.ModelAdmin):
    verbose_name = "Комментарии"
admin.site.register(Comment_post,Comments_admin)

