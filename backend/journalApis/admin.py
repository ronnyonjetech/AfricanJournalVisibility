
from django.contrib import admin



from .models import *

admin.site.register(Language)
admin.site.register(Platform)
admin.site.register(Country)
admin.site.register(Journal)
admin.site.register(ThematicArea)
admin.site.register(Volume)
admin.site.register(Article)
admin.site.register(JournalImage)
admin.site.register(LastProcessedJournal)

# Custom admin for the proxy model
class JournalsWithoutVolumesAdmin(admin.ModelAdmin):
    list_display = ('id', 'journal_title')  # Display index and journal title

# Register the proxy model with custom admin
admin.site.register(JournalsWithoutVolumes, JournalsWithoutVolumesAdmin)

class JournalsWithoutImagesAdmin(admin.ModelAdmin):
    list_display = ('id', 'journal_title')  # Show the ID and journal title
    search_fields = ('journal_title',)  # Add search functionality for journal titles
    list_filter = ('country', 'platform', 'language')  # Add filters for better navigation

    def get_queryset(self, request):
        # Override the default queryset to include only journals without images
        return JournalsWithoutImages.objects.all()

# Register the custom admin
admin.site.register(JournalsWithoutImages, JournalsWithoutImagesAdmin)


class JournalsWithoutArticlesAdmin(admin.ModelAdmin):
    list_display = ('id', 'journal_title', 'platform', 'country', 'language', 'thematic_area', 'issn_number')
    search_fields = ('journal_title', 'issn_number', 'platform__platform', 'country__country', 'language__language')
    list_filter = ('platform', 'country', 'language', 'thematic_area')
    ordering = ('journal_title',)
    readonly_fields = ('id',)

    def has_add_permission(self, request):
        # Prevent adding new instances via this proxy model
        return False

    def has_delete_permission(self, request, obj=None):
        # Prevent deleting instances via this proxy model
        return False

# Register the proxy model with the custom admin class
admin.site.register(JournalsWithoutArticles, JournalsWithoutArticlesAdmin)