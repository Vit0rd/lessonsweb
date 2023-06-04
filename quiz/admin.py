from django.contrib import admin
from .models import *

# Register your models here.
class QuizAdmin(admin.ModelAdmin):
    list_display = ('id', 'question', 'theme')
    list_display_links = ('question',)
    search_fields = ('id', 'question')

# class QuizThemeAdmin(admin.ModelAdmin):
#     list_display = ('id', 'name')
#     list_display_links = ('id', 'name')
#     search_fields = ('id', 'name')

admin.site.register(Quiz, QuizAdmin)
# admin.site.register(Quiz_theme, QuizThemeAdmin)