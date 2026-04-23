from django.shortcuts import render
from rest_framework.pagination import PageNumberPagination
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from .models import Journal, Feedback
from .serializers import (
    JournalSerializer, JournalSerializer1, LanguageSerializer, PlatformSerializer,
    CountrySerializer, ThematicAreaSerializer, VolumeSerializer, ArticleSerializer,
    VolumeSerializer1, FeedBackSerializer, CountsSerializer
)
from django.shortcuts import get_object_or_404
from django_filters.rest_framework import DjangoFilterBackend
from .filters import JournalFilter, ArticleFilter
from rest_framework import generics
from rest_framework.decorators import api_view, permission_classes
import google.generativeai as genai
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated, BasePermission
from .models import Language, Platform, Country, ThematicArea, Volume, Article
from django.db.models import Count, Q
from django.contrib.postgres.search import SearchVector, SearchQuery, SearchRank
from drf_spectacular.utils import extend_schema, extend_schema_view


# ─── Pagination ───────────────────────────────────────────────────────────────

class JournalPagination(PageNumberPagination):
    page_size_query_param = 'page_size'
    max_page_size = 100
    page_size = 10


class ArticlePagination(PageNumberPagination):
    page_size_query_param = 'page_size'
    max_page_size = 100
    page_size = 10


# ─── Journals ─────────────────────────────────────────────────────────────────

@extend_schema(
    tags=['Journals'],
    summary="List all journals (paginated)",
    description="Returns a paginated list of all approved journals. Use `page` and `page_size` query params to control pagination.",
)
class JournalPaginationListView(APIView):
    def get(self, request):
        journals = Journal.objects.all()
        paginator = JournalPagination()
        paginated_journals = paginator.paginate_queryset(journals, request)
        serializer = JournalSerializer(paginated_journals, many=True)
        return paginator.get_paginated_response(serializer.data)


@extend_schema(
    tags=['Journals'],
    summary="List journals uploaded by the authenticated user",
    description="Returns all journals uploaded by the currently authenticated user. Requires a valid JWT token.",
)
class JournalPaginationListUserView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        authenticated_user_id = request.user.id
        journals = Journal.objects.filter(user_id=authenticated_user_id)

        if not journals.exists():
            return Response({'detail': 'No journals found for the authenticated user.'}, status=status.HTTP_404_NOT_FOUND)

        serializer = JournalSerializer(journals, many=True)
        return Response(serializer.data)


@extend_schema(
    tags=['Journals'],
    summary="Search and filter journals",
    description=(
        "Search and filter journals using query parameters. "
        "Supports full-text search across title, country, language, thematic area, publisher, ISSN, platform and summary. "
        "Results are paginated and ordered by journal title."
    ),
)
class JournalSearchView(generics.ListAPIView):
    serializer_class = JournalSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = JournalFilter
    pagination_class = JournalPagination

    def get_queryset(self):
        queryset = Journal.objects.annotate(volume_count=Count('volumes')).order_by('journal_title')
        filtered_queryset = self.filter_queryset(queryset)
        if not filtered_queryset.exists():
            return queryset
        return filtered_queryset


@extend_schema(
    tags=['Journals'],
    summary="Get journal by ID",
    description="Retrieve full details of a single journal by its numeric ID.",
)
class JournalDetailView(APIView):
    def get(self, request, journal_id):
        journal = get_object_or_404(Journal, id=journal_id)
        serializer = JournalSerializer(journal)
        return Response(serializer.data)


@extend_schema(exclude=True)  # empty stub — hidden from Swagger
def getJournals(Request):
    pass


@extend_schema(
    tags=['Journals'],
    summary="Create a new journal",
    description="Submit a new journal entry. All required fields must be provided in the request body.",
)
class JournalCreateView(APIView):
    def post(self, request):
        serializer = JournalSerializer1(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# ─── Stats ────────────────────────────────────────────────────────────────────

@extend_schema(
    tags=['Stats'],
    summary="Get journal statistics",
    description=(
        "Returns aggregate counts across all journals including: "
        "open access journals, INASPS hosted, online publishers in Africa, "
        "DOAJ listings, COPE memberships, and journals with an ISSN."
    ),
)
@api_view(['GET'])
def journal_stats(request):
    stats = {
        'open_access_journal_count': Journal.objects.filter(open_access_journal=True).count(),
        'hosted_on_inasps_count': Journal.objects.filter(hosted_on_inasps=True).count(),
        'online_publisher_africa_count': Journal.objects.filter(online_publisher_africa=True).count(),
        'doaj_count': Journal.objects.filter(listed_in_doaj=True).count(),
        'cope_count': Journal.objects.filter(publisher_in_cope=True).count(),
        'issn_count': Journal.objects.filter(present_issn=True).count(),
    }
    return Response(stats)


@extend_schema(
    tags=['Stats'],
    summary="Get authenticated user's content counts",
    description="Returns the number of journals, volumes and articles uploaded by the currently authenticated user.",
)
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_user_counts(request):
    user = request.user
    return Response({
        'journals': Journal.objects.filter(user=user).count(),
        'volumes': Volume.objects.filter(journal__user=user).count(),
        'articles': Article.objects.filter(journal__user=user).count(),
    })


# ─── AI Description Generator ─────────────────────────────────────────────────

@extend_schema(
    tags=['Journals'],
    summary="Generate a journal description using AI",
    description=(
        "Accepts a journal title and uses Google Gemini AI to generate a three-paragraph "
        "description. Useful when creating or editing a journal entry."
    ),
    request={
        'application/json': {
            'type': 'object',
            'properties': {
                'journal_text': {'type': 'string', 'example': 'African Journal of Public Health'}
            },
            'required': ['journal_text']
        }
    },
)
@api_view(['POST'])
def generate_journal_description(request):
    genai.configure(api_key='AIzaSyBf6hhxPUxOgKFWnPhtgWnRj6htPPbkdWU')
    journal_text = request.data.get('journal_text')

    if not journal_text:
        return Response({"error": "Journal text is required."}, status=status.HTTP_400_BAD_REQUEST)

    try:
        model = genai.GenerativeModel("gemini-1.5-flash")
        prompt = f"Provide a brief description three paragrahs for the following journal title:'{journal_text}'."
        response = model.generate_content(prompt)

        if response and response.text:
            return Response({'journal_text': journal_text, 'description': response.text}, status=status.HTTP_200_OK)
        else:
            return Response({"error": "Failed to generate a description."}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    except Exception as e:
        return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


# ─── Reference Data ViewSets ──────────────────────────────────────────────────

@extend_schema_view(
    list=extend_schema(tags=['Languages'], summary="List all languages"),
    create=extend_schema(tags=['Languages'], summary="Create a language"),
    retrieve=extend_schema(tags=['Languages'], summary="Get a language by ID"),
    update=extend_schema(tags=['Languages'], summary="Update a language"),
    partial_update=extend_schema(tags=['Languages'], summary="Partially update a language"),
    destroy=extend_schema(tags=['Languages'], summary="Delete a language"),
)
class LanguageViewSet(viewsets.ModelViewSet):
    queryset = Language.objects.all()
    serializer_class = LanguageSerializer
    pagination_class = None


@extend_schema_view(
    list=extend_schema(tags=['Platforms'], summary="List all platforms"),
    create=extend_schema(tags=['Platforms'], summary="Create a platform"),
    retrieve=extend_schema(tags=['Platforms'], summary="Get a platform by ID"),
    update=extend_schema(tags=['Platforms'], summary="Update a platform"),
    partial_update=extend_schema(tags=['Platforms'], summary="Partially update a platform"),
    destroy=extend_schema(tags=['Platforms'], summary="Delete a platform"),
)
class PlatformViewSet(viewsets.ModelViewSet):
    queryset = Platform.objects.all()
    serializer_class = PlatformSerializer
    pagination_class = None


@extend_schema_view(
    list=extend_schema(tags=['Countries'], summary="List all countries"),
    create=extend_schema(tags=['Countries'], summary="Create a country"),
    retrieve=extend_schema(tags=['Countries'], summary="Get a country by ID"),
    update=extend_schema(tags=['Countries'], summary="Update a country"),
    partial_update=extend_schema(tags=['Countries'], summary="Partially update a country"),
    destroy=extend_schema(tags=['Countries'], summary="Delete a country"),
)
class CountryViewSet(viewsets.ModelViewSet):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer
    pagination_class = None


@extend_schema_view(
    list=extend_schema(tags=['Thematic Areas'], summary="List all thematic areas"),
    create=extend_schema(tags=['Thematic Areas'], summary="Create a thematic area"),
    retrieve=extend_schema(tags=['Thematic Areas'], summary="Get a thematic area by ID"),
    update=extend_schema(tags=['Thematic Areas'], summary="Update a thematic area"),
    partial_update=extend_schema(tags=['Thematic Areas'], summary="Partially update a thematic area"),
    destroy=extend_schema(tags=['Thematic Areas'], summary="Delete a thematic area"),
)
class ThematicAreaViewSet(viewsets.ModelViewSet):
    queryset = ThematicArea.objects.all()
    serializer_class = ThematicAreaSerializer
    pagination_class = None


# ─── Volumes ──────────────────────────────────────────────────────────────────

@extend_schema_view(
    list=extend_schema(tags=['Volumes'], summary="List all volumes"),
    create=extend_schema(tags=['Volumes'], summary="Create a volume"),
    retrieve=extend_schema(tags=['Volumes'], summary="Get a volume by ID"),
    update=extend_schema(tags=['Volumes'], summary="Update a volume"),
    partial_update=extend_schema(tags=['Volumes'], summary="Partially update a volume"),
    destroy=extend_schema(tags=['Volumes'], summary="Delete a volume"),
)
class VolumeViewSet(viewsets.ModelViewSet):
    queryset = Volume.objects.all()
    serializer_class = VolumeSerializer
    pagination_class = None


@extend_schema_view(
    list=extend_schema(
        tags=['Volumes'],
        summary="List volumes for the authenticated user",
        description="Returns all volumes belonging to journals owned by the authenticated user, including article count per volume.",
    ),
    destroy=extend_schema(
        tags=['Volumes'],
        summary="Delete a volume (owner only)",
        description="Deletes a volume. The authenticated user must own the journal the volume belongs to.",
    ),
)
class UserVolumeViewSet(viewsets.ModelViewSet):
    serializer_class = VolumeSerializer1
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Volume.objects.filter(journal__user=self.request.user).distinct()

    def list(self, request, *args, **kwargs):
        queryset = Volume.objects.filter(journal__user=request.user).annotate(
            article_count=Count('articles')
        ).distinct()
        data = [
            {
                'id': v.id,
                'journal': v.journal.journal_title,
                'volume_number': v.volume_number,
                'issue_number': v.issue_number,
                'year': v.year,
                'article_count': v.article_count,
            }
            for v in queryset
        ]
        return Response(data)

    def destroy(self, request, *args, **kwargs):
        volume = self.get_object()
        if volume.journal.user != request.user:
            return Response({"error": "You do not have permission to delete this volume."}, status=403)
        volume.delete()
        return Response({"message": "Volume deleted successfully"}, status=204)


@extend_schema(
    tags=['Volumes'],
    summary="Get volumes and articles for a journal",
    description=(
        "Returns all volumes for a given journal ID, with each volume listing its articles "
        "including title, authors, DOI, publication date, URL, PDF, and ISSN details."
    ),
)
@api_view(['GET'])
def journal_details(request, journal_id):
    try:
        journal = Journal.objects.get(id=journal_id)
    except Journal.DoesNotExist:
        return Response({"error": "Journal not found"}, status=404)

    volumes = Volume.objects.filter(journal=journal).order_by('volume_number')
    journal_data = {}

    for volume in volumes:
        articles = list(Article.objects.filter(volume=volume).values(
            "id", "title", "authors", "publication_date", "doi", "url",
            "pdf", "electronic_issn", "print_issn", "publisher"
        ))
        journal_data[f"Volume {volume.volume_number}"] = {
            "year": volume.year,
            "issue_number": volume.issue_number,
            "articles": articles,
        }

    return Response(journal_data)


# ─── Articles ─────────────────────────────────────────────────────────────────

@extend_schema_view(
    list=extend_schema(tags=['Articles'], summary="List all articles"),
    create=extend_schema(tags=['Articles'], summary="Create an article"),
    retrieve=extend_schema(tags=['Articles'], summary="Get an article by ID"),
    update=extend_schema(tags=['Articles'], summary="Update an article"),
    partial_update=extend_schema(tags=['Articles'], summary="Partially update an article"),
    destroy=extend_schema(tags=['Articles'], summary="Delete an article"),
)
class ArticleViewSet(viewsets.ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer


@extend_schema(
    tags=['Articles'],
    summary="Search and filter articles",
    description="Search and filter articles using query parameters. Results are paginated.",
)
class ArticleSearchView(generics.ListAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = ArticleFilter
    pagination_class = ArticlePagination

    def get_queryset(self):
        return super().get_queryset()


# ─── User-scoped Reference Data ───────────────────────────────────────────────

@extend_schema_view(
    list=extend_schema(
        tags=['Languages'],
        summary="List languages for the authenticated user's journals",
        description="Returns languages used across the authenticated user's journals, with a journal count per language.",
    ),
    create=extend_schema(tags=['Languages'], summary="Create a language (authenticated user)"),
    retrieve=extend_schema(tags=['Languages'], summary="Get a user language by ID"),
    update=extend_schema(tags=['Languages'], summary="Update a user language"),
    partial_update=extend_schema(tags=['Languages'], summary="Partially update a user language"),
    destroy=extend_schema(tags=['Languages'], summary="Delete a user language"),
)
class UserLanguageViewSet(viewsets.ModelViewSet):
    serializer_class = LanguageSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Language.objects.filter(journal__user=self.request.user).distinct()

    def list(self, request, *args, **kwargs):
        queryset = Language.objects.filter(journal__user=request.user).annotate(
            journal_count=Count('journal')
        ).distinct()
        data = [{'language': l.language, 'journal_count': l.journal_count} for l in queryset]
        return Response(data)


@extend_schema_view(
    list=extend_schema(
        tags=['Journals'],
        summary="List journals for the authenticated user",
        description="Returns all journals submitted by the currently authenticated user.",
    ),
    create=extend_schema(tags=['Journals'], summary="Create a journal (authenticated user)"),
    retrieve=extend_schema(tags=['Journals'], summary="Get a user journal by ID"),
    update=extend_schema(tags=['Journals'], summary="Update a user journal"),
    partial_update=extend_schema(tags=['Journals'], summary="Partially update a user journal"),
    destroy=extend_schema(tags=['Journals'], summary="Delete a user journal"),
)
class UserJournalViewSet(viewsets.ModelViewSet):
    serializer_class = JournalSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Journal.objects.filter(user=self.request.user).distinct()


@extend_schema_view(
    list=extend_schema(
        tags=['Articles'],
        summary="List articles for the authenticated user",
        description="Returns all articles belonging to journals owned by the currently authenticated user.",
    ),
    create=extend_schema(tags=['Articles'], summary="Create an article (authenticated user)"),
    retrieve=extend_schema(tags=['Articles'], summary="Get a user article by ID"),
    update=extend_schema(tags=['Articles'], summary="Update a user article"),
    partial_update=extend_schema(tags=['Articles'], summary="Partially update a user article"),
    destroy=extend_schema(tags=['Articles'], summary="Delete a user article"),
)
class UserArticleViewSet(viewsets.ModelViewSet):
    serializer_class = ArticleSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Article.objects.filter(journal__user=self.request.user).distinct()


@extend_schema_view(
    list=extend_schema(
        tags=['Thematic Areas'],
        summary="List thematic areas for the authenticated user's journals",
        description="Returns thematic areas used across the authenticated user's journals, with a journal count per thematic area.",
    ),
    create=extend_schema(tags=['Thematic Areas'], summary="Create a thematic area (authenticated user)"),
    retrieve=extend_schema(tags=['Thematic Areas'], summary="Get a user thematic area by ID"),
    update=extend_schema(tags=['Thematic Areas'], summary="Update a user thematic area"),
    partial_update=extend_schema(tags=['Thematic Areas'], summary="Partially update a user thematic area"),
    destroy=extend_schema(tags=['Thematic Areas'], summary="Delete a user thematic area"),
)
class UserThematicAreaViewSet(viewsets.ModelViewSet):
    serializer_class = ThematicAreaSerializer
    permission_classes = [IsAuthenticated]
    pagination_class = None

    def get_queryset(self):
        return ThematicArea.objects.filter(journal__user=self.request.user).distinct()

    def list(self, request, *args, **kwargs):
        queryset = ThematicArea.objects.filter(journal__user=request.user).annotate(
            journal_count=Count('journal')
        ).distinct()
        data = [{'thematic_area': t.thematic_area, 'journal_count': t.journal_count} for t in queryset]
        return Response(data)


# ─── Feedback ─────────────────────────────────────────────────────────────────

@extend_schema_view(
    list=extend_schema(tags=['Feedback'], summary="List all feedback"),
    create=extend_schema(tags=['Feedback'], summary="Submit feedback"),
    retrieve=extend_schema(tags=['Feedback'], summary="Get feedback by ID"),
    update=extend_schema(tags=['Feedback'], summary="Update feedback"),
    partial_update=extend_schema(tags=['Feedback'], summary="Partially update feedback"),
    destroy=extend_schema(tags=['Feedback'], summary="Delete feedback"),
)
class FeedbackViewSet(viewsets.ModelViewSet):
    queryset = Feedback.objects.all()
    serializer_class = FeedBackSerializer


# ─── Country Count ────────────────────────────────────────────────────────────

@extend_schema(
    tags=['Countries'],
    summary="Get journal count per country",
    description=(
        "Returns a list of countries with the number of journals per country. "
        "Supports the same search and filter parameters as the journal search endpoint. "
        "Results are ordered by journal count descending."
    ),
)
class JournalCountryCountAPIView(APIView):
    def get(self, request, *args, **kwargs):
        filtered_queryset = JournalFilter(request.GET, queryset=Journal.objects.all()).qs

        query = request.GET.get("query", "")
        if query:
            search_query = SearchQuery(query)
            search_vector = SearchVector(
                'journal_title', 'summary', 'h_index', 'platform__platform',
                'country__country', 'publishers_name', 'thematic_area__thematic_area',
                'issn_number', 'language__language'
            )
            filtered_queryset = filtered_queryset.annotate(
                rank=SearchRank(search_vector, search_query)
            ).filter(
                Q(rank__gte=0.1) |
                Q(journal_title__icontains=query) |
                Q(platform__platform__icontains=query) |
                Q(country__country__icontains=query) |
                Q(publishers_name__icontains=query) |
                Q(thematic_area__thematic_area__icontains=query) |
                Q(issn_number__icontains=query) |
                Q(language__language__icontains=query) |
                Q(h_index__icontains=query) |
                Q(summary__icontains=query)
            ).order_by('-rank').distinct()

        country_counts = (
            filtered_queryset
            .values("country__country")
            .annotate(journal_count=Count("id", distinct=True))
            .order_by("-journal_count")
        )

        formatted_data = [
            {"country": item["country__country"], "journal_count": item["journal_count"]}
            for item in country_counts
        ]
        return Response(formatted_data)


# ─── Staff / Approval Views ───────────────────────────────────────────────────

class IsStaffAndActive(BasePermission):
    message = 'Access denied. You must be an active staff member to view this resource.'

    def has_permission(self, request, view):
        return (
            request.user and
            request.user.is_authenticated and
            request.user.is_staff and
            request.user.is_active
        )


class UnapprovedJournalPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 100


@extend_schema(
    tags=['Journals'],
    summary="List all unapproved journals (staff only)",
    description="Returns a paginated list of journals pending approval. Accessible only by active staff members.",
)
class UnapprovedJournalListView(APIView):
    permission_classes = [IsStaffAndActive]

    def get(self, request):
        journals = Journal.objects.filter(approved=False).order_by('id')
        paginator = UnapprovedJournalPagination()
        paginated_journals = paginator.paginate_queryset(journals, request)
        serializer = JournalSerializer(paginated_journals, many=True)
        return paginator.get_paginated_response(serializer.data)


@extend_schema(
    tags=['Journals'],
    summary="Get a single unapproved journal (staff only)",
    description="Retrieve details of a specific unapproved journal by ID. Accessible only by active staff members.",
)
class UnapprovedJournalDetailView(APIView):
    permission_classes = [IsStaffAndActive]

    def get(self, request, journal_id):
        try:
            journal = Journal.objects.get(id=journal_id, approved=False)
        except Journal.DoesNotExist:
            return Response({'error': 'Unapproved journal not found.'}, status=status.HTTP_404_NOT_FOUND)

        serializer = JournalSerializer(journal)
        return Response(serializer.data)


@extend_schema(
    tags=['Journals'],
    summary="Approve a journal (staff only)",
    description="Sets a journal's `approved` field to `True`. Only accessible by active staff members.",
)
class ApproveJournalView(APIView):
    permission_classes = [IsStaffAndActive]

    def patch(self, request, journal_id):
        try:
            journal = Journal.objects.get(id=journal_id)
        except Journal.DoesNotExist:
            return Response({'error': 'Journal not found.'}, status=status.HTTP_404_NOT_FOUND)

        if journal.approved:
            return Response({'message': 'Journal is already approved.'}, status=status.HTTP_200_OK)

        journal.approved = True
        journal.save(update_fields=['approved'])
        return Response(
            {'message': f'Journal "{journal.journal_title}" has been approved successfully.'},
            status=status.HTTP_200_OK
        )