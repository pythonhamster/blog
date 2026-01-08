from django.shortcuts import render

# projects/views.py
from django.views.generic import ListView, DetailView
from .models import Project

class ProjectListView(ListView):
    model = Project
    template_name = "projects/project_list.html"
    context_object_name = "projects"
    extra_context = {"site_title": "Blog Spot"}

    def get_queryset(self):
        return Project.objects.prefetch_related("developers").order_by("-id")

class ProjectDetailView(DetailView):
    model = Project
    template_name = "projects/project_detail.html"
    context_object_name = "project"
    extra_context = {"site_title": "Blog Spot"}

    def get_queryset(self):
        return Project.objects.prefetch_related("developers")
