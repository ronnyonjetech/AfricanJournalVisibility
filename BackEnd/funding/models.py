from django.db import models
# from django.contrib.auth.models import User
from django.conf import settings



class FundingType(models.Model):
    name = models.CharField(max_length=255, unique=True, help_text="Type of funding (e.g., Grant, Fellowship, Scholarship).")

    def __str__(self):
        return self.name



class Funding(models.Model):
    # List of currency symbols
    CURRENCY_CHOICES = [
        ('$', 'USD ($)'),
        ('€', 'EUR (€)'),
        ('£', 'GBP (£)'),
        ('KSh', 'KES (KSh)'),
        ('₹', 'INR (₹)'),
        ('¥', 'JPY (¥)'),
        ('R', 'ZAR (R)'),
        # Add more currencies as needed
    ]

    funding_title = models.CharField(max_length=1055, help_text="Title of the funding opportunity.")
    organization = models.CharField(max_length=1055, help_text="Name of the funding organization.")
    theme = models.CharField(max_length=1055, help_text="Thematic area of the funding.")
    country = models.CharField(max_length=255, help_text="Country where the funding is applicable.")
    region = models.CharField(
        max_length=255, blank=True, null=True, 
        help_text="Region for the funding (e.g., Africa, Asia, Europe)."
    )
    funding_type = models.ForeignKey(FundingType, on_delete=models.SET_NULL, null=True, blank=True, help_text="Type of funding.")
    description = models.TextField(blank=True, null=True, help_text="Detailed description of the funding.")
    elligibility = models.TextField(blank=True, null=True, help_text="Eligibility criteria for applicants.")
    currency = models.CharField(
        max_length=5,
        choices=CURRENCY_CHOICES,
        blank=True,
        null=True,
        help_text="Currency symbol for the grant amount (e.g., $, €, £)."
    )
    grant_amount = models.DecimalField(
        max_digits=15, decimal_places=2, blank=True, null=True, 
        help_text="Amount of the grant (if applicable)."
    )
    application_link = models.URLField(blank=True, null=True, help_text="Link to apply for the funding.")
    start_date = models.DateField(blank=True, null=True, help_text="Start date for applications.")
    end_date = models.DateField(blank=True, null=True, help_text="End date for applications.")
    deadline = models.DateField(blank=True, null=True, help_text="Deadline for submitting applications.")
    is_active = models.BooleanField(default=True, help_text="Is the funding opportunity currently open?")
    status = models.CharField(
        max_length=50, choices=[('Draft', 'Draft'), ('Open', 'Open'), ('Closed', 'Closed')], 
        default='Draft', help_text="Status of the funding opportunity."
    )
    contact_email = models.EmailField(blank=True, null=True, help_text="Contact email for inquiries.")
    contact_phone = models.CharField(max_length=20, blank=True, null=True, help_text="Contact phone number.")
    attachment = models.FileField(upload_to='funding_attachments/', blank=True, null=True, help_text="Upload related document.")
    tags = models.CharField(max_length=255, blank=True, null=True, help_text="Keywords for filtering.")
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, help_text="Timestamp when this entry was created.")
    updated_at = models.DateTimeField(auto_now=True, help_text="Timestamp when this entry was last updated.")

    class Meta:
        verbose_name = "Funding Opportunity"
        verbose_name_plural = "Funding Opportunities"

    def __str__(self):
        return self.funding_title
