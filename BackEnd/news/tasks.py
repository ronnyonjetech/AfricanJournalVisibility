from __future__ import absolute_import,unicode_literals

from celery import shared_task
from django.core.management import call_command
from datetime import datetime, timedelta
# @shared_task
# def add(x,y):
#     return x+y

# @shared_task
# def run_custom_command():
#     call_command('send_newsletter')

# @shared_task
# def journal_images_generator():
#     call_command('fetch_journal_images')

@shared_task
def run_custom_command():
    today = datetime.today()
    # Check if today is the last day of the month
    if today.day == (today.replace(day=28) + timedelta(days=4)).day:
        # Run the management command if it's the last day
        call_command('send_newsletter')