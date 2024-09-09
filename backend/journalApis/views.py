from django.shortcuts import render

# Create your views here.
# Create your views here.
# views.py
from rest_framework.pagination import PageNumberPagination
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Journal
from .serializers import JournalSerializer
from django.shortcuts import get_object_or_404
from django_filters.rest_framework import DjangoFilterBackend
from .filters import JournalFilter
from rest_framework import generics





class JournalPagination(PageNumberPagination):
    # Set the page size here or in settings.py
    page_size_query_param = 'page_size'
    max_page_size = 100
    page_size = 10 


class JournalPaginationListView(APIView):
    def get(self, request):
        # Retrieve all journals from the database
        journals = Journal.objects.all()

        # Instantiate the pagination class
        paginator = JournalPagination()
        
        # Paginate the queryset
        paginated_journals = paginator.paginate_queryset(journals, request)
        
        # Serialize the journals
        serializer = JournalSerializer(paginated_journals, many=True)
        
        # Return the serialized data with pagination information
        return paginator.get_paginated_response(serializer.data)
    



class JournalSearchView(generics.ListAPIView):
    queryset = Journal.objects.all()
    serializer_class = JournalSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = JournalFilter
    pagination_class = JournalPagination


class JournalDetailView(APIView):
    def get(self, request, journal_id):
        # Retrieve the article with the specified ID
        journal = get_object_or_404(Journal, id=journal_id)
        
        # Serialize the article
        serializer = JournalSerializer(journal)
        
        # Return the serialized article data
        return Response(serializer.data)


def getJournals(Request):
    pass