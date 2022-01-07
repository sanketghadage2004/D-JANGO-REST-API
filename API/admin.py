from django.contrib import admin
from django.contrib.admin.options import ModelAdmin
from django.db import models
from .models import Blog
# Register your models here.


class BlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'status',)
     
admin.site.register(Blog ,BlogAdmin)