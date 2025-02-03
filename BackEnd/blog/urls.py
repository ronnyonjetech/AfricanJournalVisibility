from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BlogViewSet

# Create a router and register our viewset
router = DefaultRouter()
router.register(r'blogs', BlogViewSet)

urlpatterns = [
    path('', include(router.urls)),  # Includes all routes from the router
]
