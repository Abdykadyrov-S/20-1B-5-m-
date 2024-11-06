from django.contrib import admin
from .models import Settings

# Register your models here.
@admin.register(Settings)
class SettingsAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'description')
    search_fields = ('title', 'description')
    list_filter = ('id', 'title')


# admin.site.register(Settings)
