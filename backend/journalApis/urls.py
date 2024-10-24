from . import views
from django.urls import path
from .views import generate_journal_description
from .views import JournalPaginationListView,JournalSearchView,JournalDetailView,JournalCreateView,JournalPaginationListUserView
from .views import LanguageViewSet,PlatformViewSet,CountryViewSet,ThematicAreaViewSet,VolumeViewSet,ArticleViewSet  # Import your viewset

# Create individual views for list and detail actions
language_list = LanguageViewSet.as_view({
    'get': 'list',
    'post': 'create'
})

language_detail = LanguageViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})


platform_list=PlatformViewSet.as_view({
    'get': 'list',
    'post': 'create'
})

platform_detail=PlatformViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})


country_list=CountryViewSet.as_view({
    'get': 'list',
    'post': 'create'
})

country_detail=CountryViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})


thematic_list=ThematicAreaViewSet.as_view({
    'get': 'list',
    'post': 'create'
})

thematic_detail=ThematicAreaViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})

volume_list=VolumeViewSet.as_view({
    'get': 'list',
    'post': 'create'
})

volume_detail=VolumeViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})

article_list=ArticleViewSet.as_view({
    'get': 'list',
    'post': 'create'
})

article_detail=ArticleViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})

urlpatterns=[
   path('',views.getJournals),
   
   #search journals
   path('journals/', JournalPaginationListView.as_view(), name='journal-list'),
   path('user/journals/', JournalPaginationListUserView.as_view(), name='journaluser-list'),
   path('journals/search/',JournalSearchView.as_view()),
   path('api/journals/<int:journal_id>/', JournalDetailView.as_view()),
   path('journal_stats/', views.journal_stats),
   path('generate-description/', generate_journal_description, name='generate-description'),
   path('api/journalcreate/', JournalCreateView.as_view(), name='journal-create'),

   path('api/languages/', language_list, name='language-list'),  # List and create languages
   path('api/languages/<int:pk>/', language_detail, name='language-detail'),  # Retrieve, update, delete specific language
   
   path('api/platform/', platform_list, name='platform-list'),  # List and create languages
   path('api/platform/<int:pk>/', platform_detail, name='platform-detail'),  # Retrieve, update, delete specific language
   
   path('api/country/', country_list, name='country-list'),  # List and create languages
   path('api/country/<int:pk>/', country_detail, name='country-detail'),  # Retrieve, update, delete specific language

   path('api/thematic/', thematic_list, name='thematic-list'),  # List and create languages
   path('api/thematic/<int:pk>/', thematic_detail, name='thematic-detail'),  # Retrieve, update, delete specific language

   path('api/volume/', volume_list, name=' volume-list'),  # List and create languages
   path('api/volume/<int:pk>/', volume_detail, name='volume-detail'),  # Retrieve, update, delete specific language

   path('api/article/', article_list, name='article-list'),  # List and create languages
   path('api/article/<int:pk>/', article_detail, name='article-detail'),  # Retrieve, update, delete specific language
]
