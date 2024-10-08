from . import views
from django.urls import path
from .views import generate_journal_description
from .views import JournalPaginationListView,JournalSearchView,JournalDetailView
urlpatterns=[
   path('',views.getJournals),
   
   #search journals
   path('journals/', JournalPaginationListView.as_view(), name='journal-list'),
   path('journals/search/',JournalSearchView.as_view()),
   path('api/journals/<int:journal_id>/', JournalDetailView.as_view()),
   path('journal_stats/', views.journal_stats),
   path('generate-description/', generate_journal_description, name='generate-description'),
]
