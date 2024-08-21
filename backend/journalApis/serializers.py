from rest_framework import serializers
from .models import Journal,Language,Platform,Country,ThematicArea



class LanguageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Language
        fields = '__all__'

class PlatformSerializer(serializers.ModelSerializer):
    class Meta:
        model = Platform
        fields = '__all__'

class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = '__all__'

class ThematicAreaSerializer(serializers.ModelSerializer):
    class Meta:
        model = ThematicArea
        fields = '__all__'


class JournalSerializer(serializers.ModelSerializer):
    language=LanguageSerializer()
    platform=PlatformSerializer()
    country=CountrySerializer()
    thematic_area=ThematicAreaSerializer()
    class Meta:
        model = Journal
        fields = '__all__'  