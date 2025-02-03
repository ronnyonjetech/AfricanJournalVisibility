from django.contrib import admin
from .models import Blog

@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ("blog_title", "blog_link", "date_published", "created_at", "updated_at")
    search_fields = ("blog_title", "description")
    list_filter = ("date_published", "created_at", "updated_at")
    readonly_fields = ("created_at", "updated_at")
    ordering = ("-date_published",)  # Show the latest published blogs first
