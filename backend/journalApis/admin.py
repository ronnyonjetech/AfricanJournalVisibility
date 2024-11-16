
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