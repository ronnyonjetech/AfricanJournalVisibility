from __future__ import absolute_import,unicode_literals

from celery import shared_task
from django.core.management import call_command

# @shared_task
# def add(x,y):
#     return x+y

@shared_task
def run_custom_command():
    call_command('send_newsletter')

@shared_task
def journal_images_generator():
    call_command('fetch_journal_images')

