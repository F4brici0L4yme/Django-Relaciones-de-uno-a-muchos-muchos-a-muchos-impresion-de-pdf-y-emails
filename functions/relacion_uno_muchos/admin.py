from django.contrib import admin

from django.contrib import admin
from .models import Language, Framework

@admin.register(Language)
class LanguageAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

@admin.register(Framework)
class FrameworkAdmin(admin.ModelAdmin):
    list_display = ('name', 'language')
    search_fields = ('name',)
    list_filter = ('language',)
