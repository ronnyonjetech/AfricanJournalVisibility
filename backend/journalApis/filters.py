import django_filters
from django.db.models import Q
from .models import Article

class ArticleFilter(django_filters.FilterSet):
    query = django_filters.CharFilter(method='custom_search', label='Search')

    class Meta:
        model = Article
        fields = []

    def custom_search(self, queryset, name, value):
        # Perform a case-insensitive search on title, authors, and keywords
        return queryset.filter(
            Q(title__icontains=value) |
            Q(authors__icontains=value) |
            Q(keywords__icontains=value)
        )
