from django.contrib import admin
from .models import *


@admin.register(NewsItem)
class NewsItemAdmin(admin.ModelAdmin):
    pass