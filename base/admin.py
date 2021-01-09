from django.contrib import admin
from base.models import *

# Register your models here.

admin.site.register(Class_list)
admin.site.register(Subject)

@admin.register(Chapter)
class ChapterAdmin(admin.ModelAdmin):
    list_display = ('subject','chapter')


@admin.register(Material)
class MaterialAdmin(admin.ModelAdmin):
    list_display = ('chapter','name','link')