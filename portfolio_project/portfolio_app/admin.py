from django.contrib import admin

# Register your models here.

from .models import Project

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ['title', 'created_at']  # Columns in admin list
    search_fields = ['title', 'description']  # Search box
    readonly_fields = ['created_at']  # Timestamp not editable