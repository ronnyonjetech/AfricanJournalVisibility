from django.shortcuts import render

# views.py
from rest_framework import generics
from .models import Newsletter
from .serializers import NewsletterSerializer

class NewsletterListAPIView(generics.ListAPIView):
    queryset = Newsletter.objects.filter(is_published=True).order_by('-published_date')
    serializer_class = NewsletterSerializer

class NewsletterDetailAPIView(generics.RetrieveAPIView):
    queryset = Newsletter.objects.filter(is_published=True)
    serializer_class = NewsletterSerializer

