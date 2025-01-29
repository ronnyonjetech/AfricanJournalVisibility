import logging
import time
import requests
from django.core.management.base import BaseCommand
from django.core.files import File
from io import BytesIO
from tqdm import tqdm
from duckduckgo_search import DDGS
from journalApis.models import Journal, JournalImage

# Configure logging
logging.basicConfig(
    filename='journal_image_import.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

class Command(BaseCommand):
    help = 'Fetch journal images using DuckDuckGo image search and save to JournalImage model'

    VALID_EXTENSIONS = {"jpg", "jpeg", "png", "gif", "bmp", "webp"}
    QUERY_DELAY = 1  # Delay between queries in seconds to respect DuckDuckGo's server load.

    def handle(self, *args, **kwargs):
        journals = Journal.objects.filter(image__isnull=True).order_by('journal_title')
        self.stdout.write(self.style.SUCCESS(f"Found {journals.count()} journals without images."))

        for count, journal in enumerate(tqdm(journals, desc="Processing journals"), start=1):
            image_url = self.get_image_from_journal_title(journal.journal_title)

            if image_url:
                self.save_journal_image(journal, image_url)
            else:
                logging.info(f"No valid image found for journal: {journal.journal_title}")
                self.stdout.write(self.style.WARNING(f"No valid image found for journal: {journal.journal_title}"))

            self.stdout.write(self.style.SUCCESS(f"Processed journal: {journal.journal_title}"))

            # Delay to avoid overwhelming the DuckDuckGo service
            time.sleep(self.QUERY_DELAY)

            # Stop after processing 100 journals as a safety limit
            # if count >= 100:
            #     self.stdout.write(self.style.SUCCESS("Terminating after processing 100 journals."))
            #     break

    def get_image_from_journal_title(self, journal_title):
        try:
            with DDGS() as ddgs:
                results = ddgs.images(journal_title, safesearch="Moderate", max_results=10)
                for result in results:
                    image_url = result["image"]
                    if self.is_valid_image(image_url):
                        logging.info(f"Found valid image for {journal_title}: {image_url}")
                        return image_url
            logging.warning(f"No valid image found for journal: {journal_title}")
        except Exception as e:
            logging.error(f"Error fetching image for {journal_title}: {e}")
        return None

    def is_valid_image(self, url):
        """Check if the URL ends with a valid image extension."""
        return any(url.lower().endswith(f".{ext}") for ext in self.VALID_EXTENSIONS)

    def save_journal_image(self, journal, image_url):
        try:
            image_response = requests.get(image_url, stream=True)
            if image_response.status_code == 200:
                content_type = image_response.headers.get("Content-Type", "").lower()
                if not any(ext in content_type for ext in self.VALID_EXTENSIONS):
                    logging.warning(f"Invalid content type for image URL: {image_url}")
                    self.stdout.write(self.style.WARNING(f"Invalid content type for image URL: {image_url}"))
                    return

                image_name = image_url.split("/")[-1]
                image_file = BytesIO(image_response.content)

                journal_image, created = JournalImage.objects.update_or_create(
                    journal=journal,
                    defaults={'description': f"Image for {journal.journal_title} from DuckDuckGo"},
                )

                journal_image.image.save(image_name, File(image_file), save=True)
                logging.info(f"Image saved for journal: {journal.journal_title}")
                self.stdout.write(self.style.SUCCESS(f"Image saved for journal: {journal.journal_title}"))
            else:
                logging.warning(f"Failed to download image for journal: {journal.journal_title} - Status code: {image_response.status_code}")
                self.stdout.write(self.style.WARNING(f"Failed to download image for journal: {journal.journal_title}"))

        except Exception as e:
            logging.error(f"Error saving image for journal {journal.journal_title}: {e}")
            self.stdout.write(self.style.ERROR(f"Error saving image for journal {journal.journal_title}: {e}"))
