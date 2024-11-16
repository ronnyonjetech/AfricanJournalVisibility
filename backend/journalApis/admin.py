
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