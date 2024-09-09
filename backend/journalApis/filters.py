import django_filters
from django.db.models import Q
from .models import  Journal
from django.contrib.postgres.search import SearchVector,SearchQuery, SearchRank

class JournalFilter(django_filters.FilterSet):
    query = django_filters.CharFilter(method='custom_search', label='Search')
    directory_of_african_journals = django_filters.BooleanFilter(field_name='listed_in_doaj')
    Present_on_ISSN = django_filters.BooleanFilter(field_name='present_issn')
    african_index_medicus=django_filters.BooleanFilter(field_name='aim_identifier')
    indexed_on_google_scholar=django_filters.BooleanFilter(field_name='google_scholar_index')
    open_access_journal=django_filters.BooleanFilter(field_name='open_access_journal')
    member_of_Committee_on_publication_Ethics =django_filters.BooleanFilter(field_name='publisher_in_cope')
    online_publisher_in_africa=django_filters.BooleanFilter(field_name='online_publisher_africa')
    hosted_on_INASPS=django_filters.BooleanFilter(field_name='hosted_on_inasps')
    
    class Meta:
        model = Journal
        fields = []

    #Using icontains to search
    '''

    contains vs icontains
    ----------------------------------------------------------------
    *contains is case sensitive while icontains is case insensitive
    ----------------------------------------------------------------

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


    ---------------------------------------------------------------------
    Using Postgres searchVector lookup
    ---------------------------------------------------------------------
    def custom_search(self, queryset, name, value):
        # Annotating the queryset with SearchVector for full-text search
        return queryset.annotate(
            search=SearchVector(
                'journal_title',
                'platform__platform',
                'country__country',
                'publishers_name',
                'thematic_area__thematic_area',
                'issn_number',
                'language__language'
            ),
        ).filter(search=value).distinct()

    '''
    def custom_search(self, queryset, name, value):
        # Create a SearchQuery for the full-text search
        search_query = SearchQuery(value)

        # Full-text search vector
        search_vector = SearchVector(
            'journal_title',
            'platform__platform',
            'country__country',
            'publishers_name',
            'thematic_area__thematic_area',
            'issn_number',
            'language__language'
        )

        # Annotate queryset with SearchRank for full-text search relevance ranking
        queryset = queryset.annotate(
            rank=SearchRank(search_vector, search_query)
        )

        # Perform both full-text search and partial matching
        return queryset.filter(
            Q(rank__gte=0.1) |  # Full-text search matches
            Q(journal_title__icontains=value) |
            Q(platform__platform__icontains=value) |
            Q(country__country__icontains=value) |
            Q(publishers_name__icontains=value) |
            Q(thematic_area__thematic_area__icontains=value) |
            Q(issn_number__icontains=value) |
            Q(language__language__icontains=value)|
            Q(h_index__icontains=value)
        ).order_by('-rank').distinct()

