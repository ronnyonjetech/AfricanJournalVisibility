from . import views
from django.urls import path
from .views import generate_journal_description
from .views import JournalPaginationListView,JournalSearchView,JournalDetailView,JournalCreateView,JournalPaginationListUserView,ArticleSearchView
from .views import LanguageViewSet,PlatformViewSet,CountryViewSet,ThematicAreaViewSet,VolumeViewSet,ArticleViewSet,UserLanguageViewSet,UserThematicAreaViewSet  # Import your viewset
from .views import FeedbackViewSet
from .views import JournalCountryCountAPIView
from .views import journal_details
from .views import UserArticleViewSet
from .views import UserJournalViewSet
from .views import get_user_counts
# from .views import get_all_volumes
# from .views import delete_volume
from .views import UserVolumeViewSet
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

# We are manually mapping the viewset's actions to URLs
user_language_list = UserLanguageViewSet.as_view({
    'get': 'list',
    'post': 'create'
})

user_language_detail = UserLanguageViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})

# We are manually mapping the viewset's actions to URLs
user_journal_list = UserJournalViewSet.as_view({
    'get': 'list',
    'post': 'create'
})

user_journal_detail = UserJournalViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})



# We are manually mapping the viewset's actions to URLs
user_article_list = UserArticleViewSet.as_view({
    'get': 'list',
    'post': 'create'
})

user_article_detail = UserArticleViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})

# We are manually mapping the viewset's actions to URLs
user_thematic_list = UserThematicAreaViewSet.as_view({
    'get': 'list',
    'post': 'create'
})

user_thematic_detail = UserThematicAreaViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})




feedback_list=FeedbackViewSet.as_view({
    'get': 'list',
    'post': 'create'
})

feedback_detail=FeedbackViewSet.as_view({
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
   path('articles/search/', ArticleSearchView.as_view(), name='article-search'),

   path('api/user-languages/', user_language_list, name='user-language-list'),
   path('api/user-languages/<int:pk>/', user_language_detail, name='user-language-detail'),
   
   path('api/user-articles/', user_article_list, name='user-articles-list'),
   path('api/user-articles/<int:pk>/', user_article_detail, name='user-articles-detail'),

   path('api/user-journals/', user_journal_list, name='user-journal-list'),
   path('api/user-journals/<int:pk>/', user_journal_detail, name='user-journal-detail'),

   path('api/user-thematic/', user_thematic_list, name='user-language-list'),
   path('api/user-thematic/<int:pk>/', user_thematic_detail, name='user-language-detail'),

   path('api/feedback/', feedback_list, name='feedback-list'),  # List and create languages
   path('api/feedback/<int:pk>/', feedback_detail, name='feedback-detail'),  # Retrieve, update, delete specific language
   path('api/journals/country-count/', JournalCountryCountAPIView.as_view(), name='journal-country-count'),
#    path('api/volumes/', get_all_volumes, name='get_all_volumes'),
#    path('api/volumes/<int:volume_id>/delete/', delete_volume, name='delete_volume'),
   path('api/user-volumes/', UserVolumeViewSet.as_view({'get': 'list'}), name='user-volumes-list'),
   path('api/user-volumes/<int:pk>/', UserVolumeViewSet.as_view({'delete': 'destroy'}), name='user-volumes-delete'),
   path('api/journal_volumes/<int:journal_id>/', journal_details, name='journal_details'),
   
   path('api/user-counts/', get_user_counts, name='get_user_counts')
]
