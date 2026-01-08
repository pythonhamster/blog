# views.py
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from .models import Blog

class BlogView(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = "blog/list_beautiful.html"

    def get(self, request):
        blogs = (Blog.objects
                 .filter(published="published")
                 .order_by("-created_at")
                 .select_related("author"))
        return Response({"blogs": blogs, "site_title": "Blog Spot"})

class BlogDetailView(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = "blog/detail_beautiful.html"

    def get(self, request, pk):
        blog = get_object_or_404(
            Blog.objects.select_related("author"),
            pk=pk, published="published"
        )
        related = (Blog.objects.filter(published="published")
                   .exclude(pk=pk).order_by("-created_at")[:6])
        return Response({"blog": blog, "related": related, "site_title": "Blog Spot"})
