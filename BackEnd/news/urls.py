from . import views
from django.urls import path


urlpatterns = [
    path('newsletters/', views.NewsletterListAPIView.as_view(), name='newsletter_list'),
    path('newsletters/<int:pk>/', views.NewsletterDetailAPIView.as_view(), name='newsletter_detail'),
]