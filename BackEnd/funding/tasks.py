

# from celery import shared_task
# from django.utils import timezone
# from .models import Funding

# @shared_task
# def update_funding_status():
#     """
#     Update funding status and is_active field based on the deadline, start_date, and end_date.
#     """
    
#     now = timezone.now().date()

#     # Deactivate expired funding opportunities where deadline has passed
#     Funding.objects.filter(deadline__lt=now, is_active=True).update(is_active=False, status='Closed')

#     # Activate funding opportunities where the current date is within the start and end period
#     Funding.objects.filter(start_date__lte=now, end_date__gte=now, is_active=False).update(is_active=True, status='Open')

#     # Ensure draft funding remains unchanged (optional safety check)
#     Funding.objects.filter(status="Draft").update(is_active=False)

#     return "Funding statuses updated successfully."

#------------------------------------------------------------------------------#
#     Here is the latest code                                                  #
#------------------------------------------------------------------------------#

from celery import shared_task
from django.utils import timezone
from django.db.models import Q, F
from .models import Funding

@shared_task
def update_funding_status():
    """
    Update funding status and is_active field based on the deadline, start_date, and end_date.
    """
    
    now = timezone.now().date()

    # Deactivate expired funding opportunities where deadline has passed
    Funding.objects.filter(deadline__lt=now, is_active=True).update(is_active=False, status='Closed')

    # Activate funding opportunities where the current date is within the valid funding period
    Funding.objects.filter(
        (Q(start_date__lte=now) | Q(start_date__isnull=True)),  # Allow missing start_date
        Q(end_date__gte=now),
        Q(is_active=False)
    ).update(is_active=True, status='Open')

    # Ensure draft funding remains unchanged
    Funding.objects.filter(status="Draft").update(is_active=False)

    return "Funding statuses updated successfully."
