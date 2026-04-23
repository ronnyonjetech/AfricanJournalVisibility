from django.shortcuts import render

# views.py
from rest_framework import generics
from .models import Newsletter
from .serializers import NewsletterSerializer
from drf_spectacular.utils import extend_schema


@extend_schema(
    tags=['News'],
    summary="List all published newsletters",
    description="Returns all published newsletters ordered by most recently published first.",
)
class NewsletterListAPIView(generics.ListAPIView):
    queryset = Newsletter.objects.filter(is_published=True).order_by('-published_date')
    serializer_class = NewsletterSerializer

@extend_schema(
    tags=['News'],
    summary="Get a newsletter by ID",
    description="Retrieve a single published newsletter by its ID.",
)
class NewsletterDetailAPIView(generics.RetrieveAPIView):
    queryset = Newsletter.objects.filter(is_published=True)
    serializer_class = NewsletterSerializer

