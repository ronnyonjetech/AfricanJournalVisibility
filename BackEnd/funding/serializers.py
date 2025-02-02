from rest_framework import serializers

from .models import FundingType,Funding

class FundingTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = FundingType
        fields = '__all__'  # Include all fields from FundingType

# class FundingSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Funding
#         fields = '__all__'  # Include all fields from the Funding model

class FundingSerializer(serializers.ModelSerializer):
    funding_type = FundingTypeSerializer()  # Nested serializer

    class Meta:
        model = Funding
        fields = '__all__'  # Include all fields from Funding