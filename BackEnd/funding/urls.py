from django.urls import path
from .views import FundingViewSet

funding_list = FundingViewSet.as_view({
    'get': 'list',
    'post': 'create'
})

funding_detail = FundingViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'delete': 'destroy'
})

urlpatterns = [
    path('api/', funding_list, name='funding-list'),
    path('api/<int:pk>/', funding_detail, name='funding-detail'),
]
