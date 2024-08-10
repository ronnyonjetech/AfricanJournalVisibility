
from rest_framework import serializers
from .models import Volume, Article, ArticleType




class ArticleTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ArticleType
        fields = ['id', 'article_type', 'created_at']


class ArticleSerializer(serializers.ModelSerializer):
    #volume=VolumeSerializer()
    #volume = serializers.PrimaryKeyRelatedField(read_only=True)
    volume_number = serializers.SerializerMethodField() 
    article_type=ArticleTypeSerializer()
    class Meta:
        model = Article
        fields = ['id','volume_number', 'article_type', 'title', 'authors', 'keywords', 'publication_date']
    def get_volume_number(self, obj):
        return obj.volume.volume_number
     

class VolumeSerializer(serializers.ModelSerializer):
    articles = ArticleSerializer(many=True)
    
    class Meta:
        model = Volume
        fields = ['volume_number', 'created_at', 'articles']

