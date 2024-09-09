from . import views
from django.urls import path

from .views import JournalPaginationListView,JournalSearchView,JournalDetailView
urlpatterns=[
   path('',views.getJournals),
   
   #search journals
   path('journals/', JournalPaginationListView.as_view(), name='journal-list'),
   path('journals/search/',JournalSearchView.as_view()),
   path('api/journals/<int:journal_id>/', JournalDetailView.as_view()),

]