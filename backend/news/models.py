# Create your models here.
from django.db import models
from django.utils.timezone import now
from django.conf import settings

class Newsletter(models.Model):
    title = models.CharField(max_length=255, help_text="Enter the newsletter title")
    content = models.TextField(help_text="Enter the newsletter content")
    published_date = models.DateTimeField(default=now, help_text="Publication date and time")
    is_published = models.BooleanField(default=False, help_text="Mark if the newsletter is published")

    def __str__(self):
        return self.title

class Subscriber(models.Model):
    email = models.EmailField(unique=True, help_text="Subscriber's email address")
    subscribed_date = models.DateTimeField(auto_now_add=True, help_text="Date when the subscription was created")
    is_active = models.BooleanField(default=True, help_text="Is the subscription active")

    def __str__(self):
        return self.email

class NewsletterSubscription(models.Model):
    # user=models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    newsletter = models.ForeignKey(Newsletter, on_delete=models.CASCADE, related_name="subscriptions")
    subscriber = models.ForeignKey(Subscriber, on_delete=models.CASCADE, related_name="subscriptions")
    subscribed_date = models.DateTimeField(auto_now_add=True, help_text="Date of newsletter subscription")

    class Meta:
        unique_together = ("newsletter", "subscriber")

    def __str__(self):
        return f"{self.subscriber.email} subscribed to {self.newsletter.title}"
