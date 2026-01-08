from django.contrib import admin
from .models import Author, Blog
from django.utils.text import Truncator


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ["id", "first_name", "middle_name", "last_name", "picture", "email"]


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ["id", "title", "content_snippet", "image", "published", "created_at", "author"]

    def content_snippet(self, obj):
        if obj.content:
            return Truncator(obj.content).chars(50, truncate="...")
        

