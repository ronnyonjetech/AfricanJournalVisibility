from rest_framework import serializers
from .models import Journal,Language,Platform,Country,ThematicArea,Volume, Article,JournalImage,Feedback
import re


def strip_tags(value):
    return re.sub(r'<[^>]*>', '', value)

class LanguageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Language
        fields = ['id','language']

class PlatformSerializer(serializers.ModelSerializer):
    class Meta:
        model = Platform
        fields = ['id','platform']

class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = ['id','country']

class ThematicAreaSerializer(serializers.ModelSerializer):
    class Meta:
        model = ThematicArea
        fields = ['id','thematic_area']


# Serializer for Article model
class ArticleSerializer(serializers.ModelSerializer):
    abstract = serializers.SerializerMethodField()
    # volume = serializers.SerializerMethodField()
    journal = serializers.CharField(source='volume.journal.journal_title', read_only=True)
    volume_number = serializers.CharField(source='volume.volume_number', read_only=True)  # Flat volume number
    volume_issue_number = serializers.CharField(source='volume.issue_number', read_only=True)  # Flat issue number
    volume_year = serializers.CharField(source='volume.year', read_only=True)
    country=serializers.CharField(source='volume.journal.country', read_only=True)
    thematic_area=serializers.CharField(source='volume.journal.thematic_area', read_only=True)
    language=serializers.CharField(source='volume.journal.language', read_only=True)

    class Meta:
        model = Article
        fields = [
            'id','title','authors','publisher','publication_date','doi','license_url','electronic_issn','print_issn','article_type','pdf','journal', 
            'volume_number','volume_issue_number','volume_year','country','language','thematic_area','reference_count','citation_count','abstract'
        ]
        # fields = ['id', 'title', 'authors', 'keywords','pdf','publication_date']

    def get_abstract(self, obj):
        if obj.abstract:
            return strip_tags(obj.abstract)
        return obj.abstract

    # def get_volume(self, obj):
    #     if obj.volume:
    #         return {
    #             "volume_number": obj.volume.volume_number,
    #             "issue_number": obj.volume.issue_number,
    #             "year": obj.volume.year
    #         }
    #     return None  # Return `None` if volume doesn't exist

class VolumeSerializer(serializers.ModelSerializer):
    journal_id = serializers.PrimaryKeyRelatedField(queryset=Journal.objects.all(), source='journal', write_only=True)
    articles = ArticleSerializer(many=True, read_only=True)  # Nested ArticleSerializer for read-only
    
    class Meta:
        model = Volume
        fields = ['id', 'journal_id', 'volume_number', 'issue_number', 'year','articles']
    
    def create(self, validated_data):
        return Volume.objects.create(**validated_data)


# Serializer for JournalImage model
class JournalImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = JournalImage
        fields = ['id', 'image', 'description']

class JournalSerializer(serializers.ModelSerializer):
    language=LanguageSerializer()
    platform=PlatformSerializer()
    country=CountrySerializer()
    thematic_area=ThematicAreaSerializer()
    volumes = VolumeSerializer(many=True, read_only=True)
    articles=ArticleSerializer(many=True,read_only=True)
    image = JournalImageSerializer(read_only=True)  # Only one image per journal, no 'many=True'
    class Meta:
        model = Journal
        fields = '__all__'  
        
class JournalSerializer1(serializers.ModelSerializer):
    class Meta:
        model = Journal
        fields = '__all__'

# Serializer for Article model
class FeedBackSerializer(serializers.ModelSerializer):
    class Meta:
        model = Feedback
        fields = '__all__'