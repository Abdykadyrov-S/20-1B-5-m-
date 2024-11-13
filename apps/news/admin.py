from django.contrib import admin
from apps.news.models import News
# Register your models here.

@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'is_active']
    list_filter = ['id', 'title', 'is_active']
    search_fields = ['id', 'title', 'is_active']
    list_editable = ['is_active', ]