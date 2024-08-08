from . import views
from django.urls import path
from .views import (VolumeClusterView, VolumeDetailView,VolumeDeleteView,
                    ArticleListView,ArticleDetailView,ArticleUpdateView,ArticleCreateView)

urlpatterns=[
   path('',views.getJournals),
   #url route for Volumes
   path('api/volumes/', VolumeClusterView.as_view(), name='volume-cluster-list'),
   path('api/volumes/<int:volume_number>', VolumeDetailView.as_view(), name='volume-detail'),
   path('api/volumes/<int:volume_number>/delete/', VolumeDeleteView.as_view(), name='volume-delete'),
   #url route for Articles
   path('api/articles/', ArticleListView.as_view(), name='article-list'),
   path('api/articles/<int:article_id>/', ArticleDetailView.as_view(), name='article-detail'),
   path('api/articles/<int:article_id>/update/', ArticleUpdateView.as_view(), name='article-update'),
   path('api/articles/create/', ArticleCreateView.as_view(), name='article-create'),
]