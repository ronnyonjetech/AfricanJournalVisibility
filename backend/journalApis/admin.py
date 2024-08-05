# from django.contrib import admin

# # Register your models here.

# from .models import Journal, Volume, PDF

# class PDFInline(admin.TabularInline):
#     model = PDF
#     extra = 1  # Number of empty forms to display for adding PDFs

# class VolumeAdmin(admin.ModelAdmin):
#     inlines = [PDFInline]  # Allow PDFs to be added inline with the Volume
    

# class JournalAdmin(admin.ModelAdmin):
#     list_display = ('name', 'author', 'doi', 'created_at')  # Columns to display in the admin list view
#     search_fields = ('name', 'author', 'doi')  # Searchable fields

# admin.site.register(Journal, JournalAdmin)
# admin.site.register(Volume, VolumeAdmin)
# admin.site.register(PDF)
from django.contrib import admin
from .models import Journal, Volume, PDF

@admin.register(Journal)
class JournalAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_at')  # Columns to display in the list view
    search_fields = ('name',)  # Add search functionality for the journal name

@admin.register(Volume)
class VolumeAdmin(admin.ModelAdmin):
    list_display = ('journal', 'volume_number', 'created_at')  # Display volume number and journal
    list_filter = ('journal',)  # Filter by journal in the admin interface

@admin.register(PDF)
class PDFAdmin(admin.ModelAdmin):
    list_display = ('title', 'volume', 'author', 'doi', 'language', 'created_at')  # Display PDF details
    search_fields = ('title', 'author', 'doi')  # Add search functionality for title, author, and DOI
    list_filter = ('volume', 'language')  # Filter by volume and language

