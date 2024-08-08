# serializers.py

# from rest_framework import serializers
# from .models import Journal,PDF,Volume

# class JournalSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Journal
#         fields = '__all__'  # Use '__all__' to include all fields, or specify them explicitly
        
# class VolumeSerializer(serializers.ModelSerializer):
#     journal=JournalSerializer()
#     class Meta:
#         model = Volume
#         fields = '__all__'  # Use '__all__' to include all fields, or specify them explicitly
# class PDFSerializer(serializers.ModelSerializer):
#     volume=VolumeSerializer()
#     class Meta:
#         model = PDF
#         fields = '__all__'  # Use '__all__' to include all fields, or specify them explicitly