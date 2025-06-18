# urls.py
from django.urls import path
from .views import BlogView

urlpatterns = [
    path('api/blogs/', BlogView.as_view(), name='api_blog_list'),
]
