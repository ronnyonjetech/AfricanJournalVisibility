import django_filters
from django.db.models import Q
from .models import  Journal


class JournalFilter(django_filters.FilterSet):
    query = django_filters.CharFilter(method='custom_search', label='Search')
    is_listed_in_doaj = django_filters.BooleanFilter(field_name='listed_in_doaj')

    class Meta:
        model = Journal
        fields = []

    def custom_search(self, queryset, name, value):
        return queryset.filter(
            Q(journal_title__icontains=value) |
            Q(platform__platform__icontains=value) |
            Q(country__country__icontains=value) |
            Q(publishers_name__icontains=value) |
            Q(thematic_area__thematic_area__icontains=value) |
            Q(issn_number__icontains=value) |
            Q(language__language__icontains=value)
        ).distinct()