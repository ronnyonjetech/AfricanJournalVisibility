from django.shortcuts import render

# Create your views here.
# Create your views here.
# views.py

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Volume
from .serializers import VolumeSerializer, ArticleSerializer
from django.shortcuts import get_object_or_404
#from .models import Journal,PDF,Volume
#from .serializers import JournalSerializer,PDFSerializer,VolumeSerializer

# class JournalList(APIView):
#     def get(self, request):
#         journals = Journal.objects.all()  # Retrieve all Journal objects
#         serializer = JournalSerializer(journals, many=True)  # Serialize the queryset
#         return Response(serializer.data, status=status.HTTP_200_OK)  # Return serialized data
# class PDFList(APIView):
#     def get(self, request):
#         pdfs = PDF.objects.all()  # Retrieve all PDF objects
#         serializer = PDFSerializer(pdfs, many=True)  # Serialize the queryset
#         return Response(serializer.data, status=status.HTTP_200_OK)  # Return serialized data
# class VolumeList(APIView):
#     def get(self, request):
#         volumes = Volume.objects.all()  # Retrieve all Volume objects
#         serializer = VolumeSerializer(volumes, many=True)  # Serialize the queryset
#         return Response(serializer.data, status=status.HTTP_200_OK)  # Return serialized data  

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
         
def getJournals(Request):
    pass