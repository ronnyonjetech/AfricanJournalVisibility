
# Register your models here.
from django.contrib import admin
from .models import Funding

@admin.register(Funding)
class FundingAdmin(admin.ModelAdmin):
    list_display = (
        'funding_title',
        'organization',
        'theme',
        'country',
        'is_active',
        'deadline',
        'status',
    )
    list_filter = ('country', 'theme', 'is_active', 'status')
    search_fields = ('funding_title', 'organization', 'description', 'tags')
    ordering = ('-deadline',)  # Orders by deadline in descending order
    date_hierarchy = 'deadline'  # Adds a date hierarchy for the deadline field
