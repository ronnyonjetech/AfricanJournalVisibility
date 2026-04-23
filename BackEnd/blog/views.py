# from rest_framework import viewsets
# from .models import Blog
# from .serializers import BlogSerializer

# class BlogViewSet(viewsets.ModelViewSet):
#     queryset = Blog.objects.all()
#     serializer_class = BlogSerializer



from rest_framework import viewsets
from .models import Blog
from .serializers import BlogSerializer
from drf_spectacular.utils import extend_schema, extend_schema_view

@extend_schema_view(
    list=extend_schema(tags=['Blog'], summary="List all blog posts"),
    create=extend_schema(tags=['Blog'], summary="Create a blog post"),
    retrieve=extend_schema(tags=['Blog'], summary="Get a blog post by ID"),
    update=extend_schema(tags=['Blog'], summary="Update a blog post"),
    partial_update=extend_schema(tags=['Blog'], summary="Partially update a blog post"),
    destroy=extend_schema(tags=['Blog'], summary="Delete a blog post"),
)
class BlogViewSet(viewsets.ModelViewSet):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer