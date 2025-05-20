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
    journal = serializers.PrimaryKeyRelatedField(queryset=Journal.objects.all(), required=True)
    volume = serializers.PrimaryKeyRelatedField(queryset=Volume.objects.all(), required=True)

    abstract = serializers.SerializerMethodField()
    # volume = serializers.SerializerMethodField()
    journal_title = serializers.CharField(source='journal.journal_title', read_only=True)
    volume_number = serializers.CharField(source='volume.volume_number', read_only=True)  # Flat volume number
    volume_issue_number = serializers.CharField(source='volume.issue_number', read_only=True)  # Flat issue number
    volume_year = serializers.CharField(source='volume.year', read_only=True)
    country=serializers.CharField(source='journal.country', read_only=True)
    thematic_area=serializers.CharField(source='journal.thematic_area', read_only=True)
    language=serializers.CharField(source='journal.language', read_only=True)

    class Meta:
        model = Article
        fields = [
            'id','journal','volume','title','authors','publisher','journal_title','publication_date','doi','license_url','electronic_issn','print_issn','article_type','pdf','journal', 
            'volume_number','volume_issue_number','volume_year','country','language','thematic_area','reference_count','citation_count','abstract'
        ]
        

    def get_abstract(self, obj):
        if obj.abstract:
            return strip_tags(obj.abstract)
        return obj.abstract

    

class VolumeSerializer(serializers.ModelSerializer):
    id = serializers.ReadOnlyField()  # Ensure 'id' is explicitly included
    journal_id = serializers.PrimaryKeyRelatedField(queryset=Journal.objects.all(), source='journal', write_only=False)
    # articles = ArticleSerializer(many=True, read_only=True)  # Nested ArticleSerializer for read-only
    
    class Meta:
        model = Volume
        fields = ['id', 'journal_id', 'volume_number', 'issue_number', 'year']
    
    def create(self, validated_data):
        return Volume.objects.create(**validated_data)



class VolumeSerializer1(serializers.ModelSerializer):
    class Meta:
        model = Volume
        fields = ['id', 'journal', 'volume_number', 'issue_number', 'year']


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
    # volumes = VolumeSerializer(many=True, read_only=True)
    # articles=ArticleSerializer(many=True,read_only=True)
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
        