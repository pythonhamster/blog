# yourapp/urls.py
from django.urls import path
from .views import BlogView, BlogDetailView

app_name = "blog"

urlpatterns = [
    path("blogs/", BlogView.as_view(), name="blog-list"),
    path("blogs/<int:pk>/", BlogDetailView.as_view(), name="blog-detail"),  # ← use pk
]
