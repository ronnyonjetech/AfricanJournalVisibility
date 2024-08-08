from django.shortcuts import render

# Create your views here.
# Create your views here.
# views.py

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Volume,Article
from .serializers import VolumeSerializer,ArticleSerializer
from django.shortcuts import get_object_or_404


class VolumeClusterView(APIView):
    def get(self, request):
        volumes = Volume.objects.all().order_by('volume_number')
        # volume_data = []
        # volume_zero_articles = []

        # Create a dictionary to group volumes by volume number
        volume_dict = {}
        for volume in volumes:
            volume_serializer = VolumeSerializer(volume)
            volume_number = volume.volume_number

            if volume_number not in volume_dict:
                volume_dict[volume_number] = {
                    'volume_number': volume_number,
                    'created_at': volume.created_at,
                    'articles': []
                }
            
            volume_dict[volume_number]['articles'].extend(volume_serializer.data['articles'])

        # Collect volume 0 articles separately
        #volume_zero_articles = volume_dict.pop(0, {}).get('articles', [])

        # Prepare the final response
        response_data = {
            "volumes": volume_dict.values(),
            #"volume_0_articles": volume_zero_articles
        }

        return Response(response_data)
    
class VolumeDetailView(APIView):
    def get(self, request, volume_number):
        # Get the volume with the specified volume number
        volume = get_object_or_404(Volume, volume_number=volume_number)
        
        # Serialize the volume
        serializer = VolumeSerializer(volume)
        
        return Response(serializer.data)

class VolumeDeleteView(APIView):
    def delete(self, request, volume_number):
        # Get the volume with the specified volume number
        volume = get_object_or_404(Volume, volume_number=volume_number)
        
        # Delete the volume
        volume.delete()
        
        # Return a response indicating successful deletion
        return Response({'message': 'Volume deleted successfully'}, status=status.HTTP_204_NO_CONTENT)

class ArticleListView(APIView):
    def get(self, request):
        # Retrieve all articles from the database
        articles = Article.objects.all()
        
        # Serialize the articles
        serializer = ArticleSerializer(articles, many=True)
        
        # Return the serialized data
        return Response(serializer.data)

class ArticleDetailView(APIView):
    def get(self, request, article_id):
        # Retrieve the article with the specified ID
        article = get_object_or_404(Article, id=article_id)
        
        # Serialize the article
        serializer = ArticleSerializer(article)
        
        # Return the serialized article data
        return Response(serializer.data)
    
class ArticleUpdateView(APIView):
    def put(self, request, article_id):
        # Retrieve the article with the specified ID
        article = get_object_or_404(Article, id=article_id)
        
        # Deserialize the incoming data
        serializer = ArticleSerializer(article, data=request.data)
        
        # Validate and save the updated article
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def patch(self, request, article_id):
        # Retrieve the article with the specified ID
        article = get_object_or_404(Article, id=article_id)
        
        # Deserialize the incoming data
        serializer = ArticleSerializer(article, data=request.data, partial=True)
        
        # Validate and save the updated article
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class ArticleCreateView(APIView):
    def post(self, request):
        # Deserialize the incoming data
        serializer = ArticleSerializer(data=request.data)
        
        # Validate and save the new article
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)    
                     
def getJournals(Request):
    pass