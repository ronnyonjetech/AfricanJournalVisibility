from django.shortcuts import render

# Create your views here.
# Create your views here.
# views.py

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
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
def getJournals(Request):
    pass