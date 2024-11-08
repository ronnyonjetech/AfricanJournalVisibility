# import requests
# from django.core.management.base import BaseCommand
# from django.core.files import File
# from django.conf import settings
# from journalApis.models import Journal, JournalImage
# from io import BytesIO

# class Command(BaseCommand):
#     help = 'Fetch journal images from Google Custom Search API and save to JournalImage model'

#     def handle(self, *args, **kwargs):
#         # Google Custom Search API key and Custom Search Engine ID (replace with your credentials)
#         api_key = 'AIzaSyBQOXTGaC-Mcg0EEcl-JAuj6_dxOThIg1U'  # Add your Google API key in settings
#         cse_id = 'f796f7d77795148d9'     # Add your Google CSE ID in settings

#         # Get all journals
#         journals = Journal.objects.all()

#         # Iterate through each journal and fetch an image
#         for journal in journals:
#             image_url = self.get_image_from_journal_title(journal.journal_title, api_key, cse_id)

#             if image_url:
#                 self.save_journal_image(journal, image_url)

#             self.stdout.write(self.style.SUCCESS(f"Processed journal: {journal.journal_title}"))

#     def get_image_from_journal_title(self, journal_title, api_key, cse_id):
#         """Fetches the image URL for a given journal title using Google Custom Search API."""
#         search_url = f'https://www.googleapis.com/customsearch/v1?q={journal_title}&cx={cse_id}&key={api_key}&searchType=image&num=1'
#         response = requests.get(search_url)

#         if response.status_code == 200:
#             search_results = response.json()
#             items = search_results.get('items', [])
#             if items:
#                 return items[0]['link']  # Return the first image link
#         self.stdout.write(self.style.WARNING(f"No image found for journal: {journal_title}"))
#         return None

#     def save_journal_image(self, journal, image_url):
#         """Saves the image URL to the JournalImage model."""
#         try:
#             # Download the image
#             image_response = requests.get(image_url)
#             if image_response.status_code == 200:
#                 image_name = image_url.split("/")[-1]  # Get image name from URL
#                 image_file = BytesIO(image_response.content)

#                 # Create or update the JournalImage model
#                 journal_image, created = JournalImage.objects.update_or_create(
#                     journal=journal,
#                     defaults={'description': f"Image for {journal.journal_title} from Google Custom Search"},
#                 )

#                 # Save the image file to the ImageField
#                 journal_image.image.save(image_name, File(image_file), save=True)

#                 self.stdout.write(self.style.SUCCESS(f"Image saved for journal: {journal.journal_title}"))
#             else:
#                 self.stdout.write(self.style.WARNING(f"Failed to download image for journal: {journal.journal_title}"))
#         except Exception as e:
#             self.stdout.write(self.style.ERROR(f"Error saving image for journal {journal.journal_title}: {e}"))



import logging
import requests
from django.core.management.base import BaseCommand
from django.core.files import File
from django.conf import settings
from journalApis.models import Journal, JournalImage
from io import BytesIO
from tqdm import tqdm

# Configure logging
logging.basicConfig(
    filename='journal_image_import.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

class Command(BaseCommand):
    help = 'Fetch journal images from Google Custom Search API and save to JournalImage model'

    def handle(self, *args, **kwargs):
        # Google Custom Search API key and Custom Search Engine ID
        api_key = 'AIzaSyBQOXTGaC-Mcg0EEcl-JAuj6_dxOThIg1U'  # Ensure this is set in settings.py
        cse_id = 'f796f7d77795148d9'     # Ensure this is set in settings.py

        # Get all journals that do not already have an associated image
        journals = Journal.objects.filter(image__isnull=True)

        self.stdout.write(self.style.SUCCESS(f"Found {journals.count()} journals without images."))

        # Iterate through each journal and fetch an image
        for journal in tqdm(journals, desc="Processing journals"):
            image_url = self.get_image_from_journal_title(journal.journal_title, api_key, cse_id)

            if image_url:
                self.save_journal_image(journal, image_url)
            else:
                # Log if no image was found and leave as null
                logging.info(f"No image found for journal: {journal.journal_title}")
                self.stdout.write(self.style.WARNING(f"No image found for journal: {journal.journal_title}"))

            self.stdout.write(self.style.SUCCESS(f"Processed journal: {journal.journal_title}"))

    def get_image_from_journal_title(self, journal_title, api_key, cse_id):
        """Fetches the image URL for a given journal title using Google Custom Search API."""
        search_url = f'https://www.googleapis.com/customsearch/v1?q={journal_title}&cx={cse_id}&key={api_key}&searchType=image&num=1'
        response = requests.get(search_url)

        if response.status_code == 200:
            search_results = response.json()
            items = search_results.get('items', [])
            if items:
                image_url = items[0]['link']  # Return the first image link
                logging.info(f"Found image for {journal_title}: {image_url}")
                return image_url
        logging.warning(f"No image found for journal: {journal_title}")
        return None

    def save_journal_image(self, journal, image_url):
        """Downloads and saves the image to the JournalImage model."""
        try:
            # Download the image
            image_response = requests.get(image_url)
            if image_response.status_code == 200:
                image_name = image_url.split("/")[-1]  # Get image name from URL
                image_file = BytesIO(image_response.content)

                # Create or update the JournalImage model with the image
                journal_image, created = JournalImage.objects.update_or_create(
                    journal=journal,
                    defaults={'description': f"Image for {journal.journal_title} from Google Custom Search"},
                )

                # Save the image file to the ImageField
                journal_image.image.save(image_name, File(image_file), save=True)

                logging.info(f"Image saved for journal: {journal.journal_title}")
                self.stdout.write(self.style.SUCCESS(f"Image saved for journal: {journal.journal_title}"))
            else:
                logging.warning(f"Failed to download image for journal: {journal.journal_title} - Status code: {image_response.status_code}")
                self.stdout.write(self.style.WARNING(f"Failed to download image for journal: {journal.journal_title}"))

        except Exception as e:
            logging.error(f"Error saving image for journal {journal.journal_title}: {e}")
            self.stdout.write(self.style.ERROR(f"Error saving image for journal {journal.journal_title}: {e}"))
