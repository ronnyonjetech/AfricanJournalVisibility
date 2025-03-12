# from __future__ import absolute_import,unicode_literals

# from celery import shared_task
# from django.core.management import call_command
# from datetime import datetime, timedelta


# @shared_task
# def run_custom_command():
#     call_command('send_newsletter')

from __future__ import absolute_import, unicode_literals

from celery import shared_task
from django.core.management import call_command
from datetime import datetime
import calendar

@shared_task
def run_custom_command():
    today = datetime.today().date()
    last_day = calendar.monthrange(today.year, today.month)[1]  # Get last day of the month

    if today.day == last_day:
        call_command('send_newsletter')  # Run the newsletter command
        print("✅ Newsletter sent on the last day of the month")
    else:
        print(f"⏩ Skipping: {today} is not the last day of the month")
