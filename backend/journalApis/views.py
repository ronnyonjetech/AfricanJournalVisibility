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



# class ArticlePagination(PageNumberPagination):
#     # page_size = 3
#     page_size_query_param = 'page_size'  # Allows clients to set the page size
#     max_page_size = 100

class JournalPagination(PageNumberPagination):
    # Set the page size here or in settings.py
    page_size_query_param = 'page_size'
    max_page_size = 100
    page_size = 10 


# class LatestVolumeView(APIView):
#     def get(self, request):
#         # Fetch the latest volume based on volume_number
#         latest_volume = Volume.objects.order_by('-volume_number').first()
        
#         if latest_volume is not None:
#             # Serialize the latest volume
#             volume_serializer = VolumeSerializer(latest_volume)
#             volume_number = latest_volume.volume_number

#             # Prepare response data
#             response_data = {
#                 'volume_number': volume_number,
#                 'created_at': latest_volume.created_at,
#                 'articles': volume_serializer.data['articles']
#             }
#         else:
#             response_data = {'error': 'No volume data available'}

#         return Response(response_data)

# class VolumeClusterView(APIView):
#     def get(self, request):
#         volumes = Volume.objects.all().order_by('volume_number')
#         # volume_data = []
#         # volume_zero_articles = []

#         # Create a dictionary to group volumes by volume number
#         volume_dict = {}
#         for volume in volumes:
#             volume_serializer = VolumeSerializer(volume)
#             volume_number = volume.volume_number

#             if volume_number not in volume_dict:
#                 volume_dict[volume_number] = {
#                     'volume_number': volume_number,
#                     'created_at': volume.created_at,
#                     'articles': []
#                 }
            
#             volume_dict[volume_number]['articles'].extend(volume_serializer.data['articles'])

#         # Collect volume 0 articles separately
#         #volume_zero_articles = volume_dict.pop(0, {}).get('articles', [])

#         # Prepare the final response
#         response_data = {
#             "volumes": volume_dict.values(),
#             #"volume_0_articles": volume_zero_articles
#         }

#         return Response(response_data)
    
# class VolumeDetailView(APIView):
#     def get(self, request, volume_number):
#         # Get the volume with the specified volume number
#         volume = get_object_or_404(Volume, volume_number=volume_number)
        
#         # Serialize the volume
#         serializer = VolumeSerializer(volume)
        
#         return Response(serializer.data)

# class VolumeDeleteView(APIView):
#     def delete(self, request, volume_number):
#         # Get the volume with the specified volume number
#         volume = get_object_or_404(Volume, volume_number=volume_number)
        
#         # Delete the volume
#         volume.delete()
        
#         # Return a response indicating successful deletion
#         return Response({'message': 'Volume deleted successfully'}, status=status.HTTP_204_NO_CONTENT)

# class ArticleListView(APIView):
#     def get(self, request):
#         # Retrieve all articles from the database
#         articles = Article.objects.all()
        
#         # Serialize the articles
#         serializer = ArticleSerializer(articles, many=True)
        
#         # Return the serialized data
#         return Response(serializer.data)

# class ArticlePaginationListView(APIView):
#     def get(self, request):
#         # Retrieve all articles from the database
#         articles = Article.objects.all()

#         # Instantiate the pagination class
#         paginator = ArticlePagination()
        
#         # Paginate the queryset
#         paginated_articles = paginator.paginate_queryset(articles, request)
#         # Serialize the articles
#         serializer = ArticleSerializer(paginated_articles, many=True)
        
#         # Return the serialized data
#         return paginator.get_paginated_response(serializer.data) 
    
# class LatestArticleListView(APIView):
#     def get(self, request):
#         # Retrieve the latest 5 articles from the database, ordered by created_at descending
#         latest_articles = Article.objects.order_by('-publication_date')[:5]
        
#         # Serialize the articles
#         serializer = ArticleSerializer(latest_articles, many=True)
        
#         # Return the serialized data
#         return Response(serializer.data)

# class ArticleDetailView(APIView):
#     def get(self, request, article_id):
#         # Retrieve the article with the specified ID
#         article = get_object_or_404(Article, id=article_id)
        
#         # Serialize the article
#         serializer = ArticleSerializer(article)
        
#         # Return the serialized article data
#         return Response(serializer.data)
    
# class ArticleUpdateView(APIView):
#     def put(self, request, article_id):
#         # Retrieve the article with the specified ID
#         article = get_object_or_404(Article, id=article_id)
        
#         # Deserialize the incoming data
#         serializer = ArticleSerializer(article, data=request.data)
        
#         # Validate and save the updated article
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
        
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
#     def patch(self, request, article_id):
#         # Retrieve the article with the specified ID
#         article = get_object_or_404(Article, id=article_id)
        
#         # Deserialize the incoming data
#         serializer = ArticleSerializer(article, data=request.data, partial=True)
        
#         # Validate and save the updated article
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
        
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
# class ArticleCreateView(APIView):
#     def post(self, request):
#         # Deserialize the incoming data
#         serializer = ArticleSerializer(data=request.data)
        
#         # Validate and save the new article
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
        
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)    
    
# #To be improved after migration to POSTGRES DATABASE
# class ArticleSearchView(generics.ListAPIView):
#     queryset = Article.objects.all()
#     serializer_class = ArticleSerializer
#     filter_backends = [DjangoFilterBackend]
#     filterset_class = ArticleFilter


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
    
# class JournalListView(generics.ListAPIView):
#     queryset = Journal.objects.all()
#     serializer_class = JournalSerializer


# class JournalListView(generics.ListAPIView):
#     queryset = Journal.objects.all()
#     serializer_class = JournalSerializer
#     filter_backends = [SearchFilter]
#     search_fields = [
#         'journal_title', 
#         'platform__platform', 
#         'country__country', 
#         'publishers_name', 
#         'language__language', 
#         'thematic_area__thematic_area',
#         'issn_number',
#         'eigen_metrix',
#         'link',
#     ]
#     pagination_class = JournalPagination  # Use the custom pagination class




# class JournalSearchView(generics.ListAPIView):
#     queryset = Journal.objects.all()
#     serializer_class = JournalSerializer
#     filter_backends = [DjangoFilterBackend]
#     filterset_class = JournalFilter


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