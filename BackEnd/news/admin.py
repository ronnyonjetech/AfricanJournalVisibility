from django.contrib import admin
from django.conf import settings
from django.template.loader import render_to_string
from django.contrib.auth import get_user_model  # This is the correct way to get the user model
from .models import Newsletter
from django.core.mail import EmailMessage,EmailMultiAlternatives
from django.utils.html import strip_tags
from django.conf import settings
from django.contrib.auth import get_user_model
import requests



def fetch_newsletter_data():
    # Fetch data from your API
    api_url = 'https://aphrc.site/news/newsletters/'
    response = requests.get(api_url)
    
    if response.status_code == 200:
        # Parse the response JSON and return it
        return response.json()
    else:
        return None

def send_html_email_to_all_users(modeladmin, request, queryset):
    # Fetch data from the API
    api_data = fetch_newsletter_data()

    # Check if we have valid data
    if api_data and 'results' in api_data:
        newsletters = api_data['results']  # Get the list of newsletters
        subject = "AfrikaJournals Latest Newsletters"  # Set a constant subject/title for the email
        # The email content can be built dynamically using the list of newsletters
        message_content = "Here is the latest newsletter:"  # You can change this text

        # Get all registered users using the custom user model
        User = get_user_model()  # Get the custom user model if it's defined
        users = User.objects.all()

        for user in users:
            # Log user details to confirm values
            print("Sending email to:", user.email)

            # Prepare context, including the list of newsletters
            context = {
                'newsletters': newsletters,  # Pass all newsletters to the template
                'user_name': user.user_name,  # Assuming 'username' is the field in your custom user model
                'message_content': message_content  # Include the general content in the HTML template
            }

            # Render the email content using the HTML template
            html_message = render_to_string("email/newsletter_email.html", context)
            plain_message = strip_tags(html_message)  # Get the plain text version of the HTML content
            print(html_message)

            # Prepare and send the email with both HTML and plain text versions
            email = EmailMultiAlternatives(
                subject=subject,
                body=plain_message,  # Leave the body empty to ensure it's sent as HTML only
                from_email=settings.DEFAULT_FROM_EMAIL,
                to=[user.email],
            )

            email.attach_alternative(html_message, "text/html")
            email.send()

        # Display a success message in the admin
        modeladmin.message_user(request, "Email sent successfully to all users.")
    else:
        # Handle the case when the API data is not available
        modeladmin.message_user(request, "Failed to fetch newsletter data.")


'''
def send_html_email_to_all_users(modeladmin, request, queryset):
    # Fetch data from the API
    
    # Loop through the selected newsletters if any (or just send a generic email)
    for newsletter in queryset:
        subject = newsletter.title  # Use the newsletter's title as the subject
        message_content = newsletter.content  # Use the content of the newsletter as the email body

        # Log the newsletter content to debug
        print("Newsletter Content:", message_content)
        
        # Get all registered users using the custom user model
        User = get_user_model()  # Get the custom user model if it's defined
        users = User.objects.all()

        for user in users:
            # Log user details to confirm values
            print("Sending email to:", user.email)

            context={
                        'newsletter': newsletter,  # Pass the entire newsletter to the template
                        'user_name': user.user_name,  # Assuming 'username' is the field in your custom user model
                        'message_content': message_content  # Include the newsletter content if needed in the HTML template
                    }
            
            # Render the email content using the HTML template
            html_message = render_to_string("email/newsletter_email.html",context)
            plain_message=strip_tags(html_message)
            print(html_message)
            email=EmailMultiAlternatives(
                subject=subject,
                body=plain_message,  # Leave the body empty to ensure it's sent as HTML only
                from_email=settings.DEFAULT_FROM_EMAIL,
                to=[user.email],
            )

            email.attach_alternative(html_message,"text/html")
            email.send()

    # Display a success message in the admin
    modeladmin.message_user(request, "Email sent successfully to all users.")
'''

# Register the action in your admin
class NewsletterAdmin(admin.ModelAdmin):
    actions = [send_html_email_to_all_users]

admin.site.register(Newsletter, NewsletterAdmin)
