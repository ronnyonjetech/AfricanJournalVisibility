from celery import shared_task
from django.utils import timezone
from .models import Funding

@shared_task
def update_funding_status():
    """
    Update funding status and is_active field based on the deadline.
    """
    
    now = timezone.now().date()

    # Deactivate expired funding opportunities
    Funding.objects.filter(deadline__lt=now, is_active=True).update(is_active=False, status='Closed')

    # Activate open funding opportunities
    Funding.objects.filter(start_date__lte=now, end_date__gte=now, is_active=False).update(is_active=True, status='Open')

    return "Funding statuses updated successfully."
