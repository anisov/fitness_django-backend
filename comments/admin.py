from django.contrib import admin
from .models import *


class CommentsAdmin(admin.ModelAdmin):
    verbose_name = "Комментарии"


admin.site.register(CommentPost, CommentsAdmin)

