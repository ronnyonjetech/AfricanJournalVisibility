from rest_framework import serializers
from .models import Newsletter, Subscriber, NewsletterSubscription

class NewsletterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Newsletter
        fields = ['id', 'title', 'content', 'published_date', 'is_published']

class SubscriberSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subscriber
        fields = ['id', 'email', 'subscribed_date', 'is_active']

class NewsletterSubscriptionSerializer(serializers.ModelSerializer):
    newsletter = NewsletterSerializer(read_only=True)
    subscriber = SubscriberSerializer(read_only=True)

    class Meta:
        model = NewsletterSubscription
        fields = ['id', 'newsletter', 'subscriber', 'subscribed_date']
