from . import views
from django.urls import path
from .views import VolumeClusterView, VolumeDetailView
# from .views import JournalList,PDFList,VolumeList
urlpatterns=[
   path('',views.getJournals),
   # path('journals/', JournalList.as_view(), name='journal-list'),
   # path('pdfs/', PDFList.as_view(), name='pdf-list'),
   # path('volumes/', VolumeList.as_view(), name='volume-list'),
   path('api/volumes/', VolumeClusterView.as_view(), name='volume-cluster-list'),
   path('api/volumes/<int:volume_number>', VolumeDetailView.as_view(), name='volume-detail'),
]