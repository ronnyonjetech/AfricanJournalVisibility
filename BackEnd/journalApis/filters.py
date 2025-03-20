import django_filters
from django.db.models import Q
from .models import  Journal,Article
# from django.contrib.postgres.search import SearchVector,SearchQuery, SearchRank
from django.contrib.postgres.search import (
    SearchVector, SearchQuery, SearchRank, SearchHeadline
)


class JournalFilter(django_filters.FilterSet):
    query = django_filters.CharFilter(method='custom_search', label='Search')
    directory_of_african_journals = django_filters.BooleanFilter(field_name='listed_in_doaj')
    present_on_issn = django_filters.BooleanFilter(field_name='present_issn')
    african_index_medicus = django_filters.BooleanFilter(field_name='aim_identifier')
    indexed_on_google_scholar = django_filters.BooleanFilter(field_name='google_scholar_index')
    open_access_journal = django_filters.BooleanFilter(field_name='open_access_journal')
    member_of_committee_on_publication_ethics = django_filters.BooleanFilter(field_name='publisher_in_cope')
    online_publisher_in_africa = django_filters.BooleanFilter(field_name='online_publisher_africa')
    hosted_on_inasps = django_filters.BooleanFilter(field_name='hosted_on_inasps')

    class Meta:
        model = Journal
        fields = []

    def custom_search(self, queryset, name, value):
        if not value:
            return queryset  # Prevent infinite recursion
        
        words = value.split()[:10]  # Limit to first 10 words

        # Use 'websearch' mode for better query interpretation
        search_query = SearchQuery(words[0], search_type='websearch')
        for word in words[1:]:
            search_query |= SearchQuery(word, search_type='websearch')

        # Define the search vector
        search_vector = SearchVector(
            'journal_title',
            'summary',
            'h_index',
            'platform__platform',
            'country__country',
            'publishers_name',
            'thematic_area__thematic_area',
            'issn_number',
            'language__language'
        )

        # Annotate queryset with SearchRank for relevance
        queryset = queryset.annotate(
            rank=SearchRank(search_vector, search_query),
            highlight=SearchHeadline('summary', search_query)  # Highlights matched text
        )

        # Perform both full-text search and partial matching
        return queryset.filter(
            Q(rank__gte=0.05) |
            Q(journal_title__icontains=value) |
            Q(platform__platform__icontains=value) |
            Q(country__country__icontains=value) |
            Q(publishers_name__icontains=value) |
            Q(thematic_area__thematic_area__icontains=value) |
            Q(issn_number__icontains=value) |
            Q(language__language__icontains=value) |
            Q(h_index__icontains=value) |
            Q(summary__icontains=value)
        ).order_by('-rank')  # Removed .distinct() to avoid recursion errors



class ArticleFilter(django_filters.FilterSet):
    # Filters for Article fields
    query = django_filters.CharFilter(method='custom_search', label='Search')

    # Filter for a specific publication date
    publication_date = django_filters.DateFilter(field_name="publication_date", label="Publication Date (Specific Day)", lookup_expr="exact")
    # Date range filter
    publication_date_range = django_filters.DateFromToRangeFilter(field_name="publication_date", label="Publication Date Range")

    class Meta:
        model = Article
        fields = []

    def custom_search(self, queryset, name, value):
        if not value:
            return queryset  # Prevent unnecessary processing

        words = value.split()[:10]  # Limit to first 10 words to prevent deep recursion

        # Use 'websearch' mode for better query interpretation
        search_query = SearchQuery(words[0], search_type='websearch')
        for word in words[1:]:
            search_query |= SearchQuery(word, search_type='websearch')

        # Define the search vector
        search_vector = SearchVector(
            'title',
            'abstract',
            'keywords',
            'authors',
            'subjects',
            'article_type',
            'publisher'
        )

        # Annotate queryset with SearchRank and SearchHeadline for better results
        queryset = queryset.annotate(
            rank=SearchRank(search_vector, search_query),
            highlight=SearchHeadline('abstract', search_query)  # Highlights matched content in abstracts
        )

        # Article and related Journal filtering
        return queryset.filter(
            Q(rank__gte=0.05) |  # Lowered threshold for better matches
            Q(title__icontains=value) |
            Q(abstract__icontains=value) |
            Q(keywords__icontains=value) |
            Q(authors__icontains=value) |
            Q(subjects__icontains=value) |
            Q(article_type__icontains=value) |
            Q(publisher__icontains=value) |
            # Related Journal fields
            Q(journal__journal_title__icontains=value) |
            Q(journal__country__country__icontains=value) |
            Q(journal__language__language__icontains=value) |
            Q(journal__thematic_area__thematic_area__icontains=value)
        ).order_by('-rank')  # Removed .distinct() to avoid recursion errors


