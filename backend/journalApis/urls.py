from . import views
from django.urls import path
# from .views import JournalList,PDFList,VolumeList
urlpatterns=[
   path('',views.getJournals),
   # path('journals/', JournalList.as_view(), name='journal-list'),
   # path('pdfs/', PDFList.as_view(), name='pdf-list'),
   # path('volumes/', VolumeList.as_view(), name='volume-list'),
]