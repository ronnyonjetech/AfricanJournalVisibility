from django.contrib import admin

# Register your models here.

from .models import Journal, Volume, PDF

class PDFInline(admin.TabularInline):
    model = PDF
    extra = 1  # Number of empty forms to display for adding PDFs

class VolumeAdmin(admin.ModelAdmin):
    inlines = [PDFInline]  # Allow PDFs to be added inline with the Volume
    

class JournalAdmin(admin.ModelAdmin):
    list_display = ('name', 'author', 'doi', 'created_at')  # Columns to display in the admin list view
    search_fields = ('name', 'author', 'doi')  # Searchable fields

admin.site.register(Journal, JournalAdmin)
admin.site.register(Volume, VolumeAdmin)
admin.site.register(PDF)
