from django.contrib import admin
from .models import *

class LessonAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'serial', 'publish', 'theme')
    list_display_links = ('name', 'theme')
    search_fields = ('id', 'name')

class ThemeAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'serial')
    list_display_links = ('name',)
    search_fields = ('id', 'name')

# Register your models here.
admin.site.register(Lesson, LessonAdmin)
admin.site.register(Theme, ThemeAdmin)