from rest_framework.views import APIView
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from .models import Blog


class BlogView(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = "blog/list.html"
    
    
    def get(self, request):
        blogs = Blog.objects.all()
        return Response({"blogs": blogs})