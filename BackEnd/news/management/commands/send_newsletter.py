from django.core.management.base import BaseCommand
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.contrib.auth import get_user_model
from django.conf import settings
import requests

class Command(BaseCommand):
    help = "Send newsletters to all users via email."

    def fetch_newsletter_data(self):
        api_url = 'https://aphrc.site/news/newsletters/'
        response = requests.get(api_url)
        
        if response.status_code == 200:
            return response.json()
        return None

    def send_html_email_to_all_users(self):
        api_data = self.fetch_newsletter_data()

        if api_data and 'results' in api_data:
            newsletters = api_data['results']
            subject = "AfrikaJournals Latest Newsletters"
            message_content = "Here is the latest newsletter:"
            
            User = get_user_model()
            user_emails = list(User.objects.values_list('email', flat=True))

            context = {
                'newsletters': newsletters,
                'message_content': message_content
            }

            html_message = render_to_string("email/newsletter_email.html", context)
            plain_message = strip_tags(html_message)

            email = EmailMultiAlternatives(
                subject=subject,
                body=plain_message,
                from_email=settings.DEFAULT_FROM_EMAIL,
                to=user_emails,  # Send to all users at once
            )
            email.attach_alternative(html_message, "text/html")
            email.send()

            self.stdout.write(self.style.SUCCESS("Email sent successfully to all users."))
        else:
            self.stdout.write(self.style.ERROR("Failed to fetch newsletter data."))

    def handle(self, *args, **kwargs):
        self.send_html_email_to_all_users()
