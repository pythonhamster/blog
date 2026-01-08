from django.contrib import admin
from .models import Project, Devloper
from django.utils.text import Truncator
from django.utils.html import format_html
# Register your models here.

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ["name", "description", "github"]

    def description_snippet(self, obj):
        if obj.description:
            return Truncator(obj.description).chars(50, truncate="...")

@admin.register(Devloper)
class DevloperAdmin(admin.ModelAdmin):
    list_display = ["first_name", "last_name", "show_avatar"]

    def show_avatar(self, obj:Devloper):
        if obj.profile_photo:
             return format_html(
                '<img src="{}" width="60" height="60" style="object-fit: cover; border-radius: 50%;" />',
                obj.profile_photo.url
            )
        return "—"  # fallback if no image
    show_avatar.short_description = "Profile Image"