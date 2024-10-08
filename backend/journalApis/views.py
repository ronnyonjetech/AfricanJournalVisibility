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
from rest_framework.decorators import api_view
import google.generativeai as genai




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



@api_view(['GET'])
def journal_stats(request):
    # Count total number of journals with specific attributes
    open_access_count = Journal.objects.filter(open_access_journal=True).count()
    hosted_on_inasps_count = Journal.objects.filter(hosted_on_inasps=True).count()
    online_publisher_africa_count = Journal.objects.filter(online_publisher_africa=True).count()
    doaj_count = Journal.objects.filter(listed_in_doaj=True).count()
    cope_count = Journal.objects.filter(publisher_in_cope=True).count()
    issn_count = Journal.objects.filter(present_issn=True).count()
    
    # Create response dictionary
    stats = {
        'open_access_journal_count': open_access_count,
        'hosted_on_inasps_count': hosted_on_inasps_count,
        'online_publisher_africa_count': online_publisher_africa_count,
        'doaj_count': doaj_count,
        'cope_count': cope_count,
        'issn_count': issn_count,
    }

    return Response(stats)

@api_view(['POST'])
def generate_journal_description(request):
    genai.configure(api_key='AIzaSyBf6hhxPUxOgKFWnPhtgWnRj6htPPbkdWU')
    # Get the journal text from the request data
    journal_text = request.data.get('journal_text')

    if not journal_text:
        return Response({"error": "Journal text is required."}, status=status.HTTP_400_BAD_REQUEST)

    try:
        # Initialize the generative model
        model = genai.GenerativeModel("gemini-1.5-flash")

        # Generate a brief description based on the input journal text
        prompt = f"Provide a brief description three paragrahs for the following journal title:'{journal_text}'."
        response = model.generate_content(prompt)

        # Check if the response contains the generated description
        if response and response.text:
            print(response.text)
            return Response({
                'journal_text': journal_text,
                'description': response.text
            }, status=status.HTTP_200_OK)
        else:
            return Response({"error": "Failed to generate a description."}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    except Exception as e:
        # Handle errors during the process
        return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

