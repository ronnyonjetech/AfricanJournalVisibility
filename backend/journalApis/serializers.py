from rest_framework import serializers
from .models import Journal,Language,Platform,Country,ThematicArea,Volume, Article,JournalImage



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


# Serializer for Article model
class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ['id', 'title', 'authors', 'keywords','pdf','publication_date']

# Serializer for Volume model, including nested articles
class VolumeSerializer(serializers.ModelSerializer):
    articles = ArticleSerializer(many=True, read_only=True)  # Nested ArticleSerializer to include all articles in this volume

    class Meta:
        model = Volume
        fields = ['id','volume_number','issue_number','year','created_at','articles']

# Serializer for JournalImage model
class JournalImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = JournalImage
        fields = ['id', 'image', 'description', 'uploaded_at']

class JournalSerializer(serializers.ModelSerializer):
    language=LanguageSerializer()
    platform=PlatformSerializer()
    country=CountrySerializer()
    thematic_area=ThematicAreaSerializer()
    volumes = VolumeSerializer(many=True, read_only=True)
    image = JournalImageSerializer(read_only=True)  # Only one image per journal, no 'many=True'
    class Meta:
        model = Journal
        fields = '__all__'  