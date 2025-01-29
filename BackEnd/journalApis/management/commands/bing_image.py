import logging
import requests
from django.core.management.base import BaseCommand
from django.core.files import File
from io import BytesIO
from tqdm import tqdm
from journalApis.models import Journal, JournalImage
from bing_image_downloader.downloader import download

# Configure logging
logging.basicConfig(
    filename='journal_image_import.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

class Command(BaseCommand):
    help = 'Fetch journal images using Bing Image Downloader and save to JournalImage model'

    def handle(self, *args, **kwargs):
        journals = Journal.objects.filter(images__isnull=True).order_by('journal_title')
        self.stdout.write(self.style.SUCCESS(f"Found {journals.count()} journals without images."))

        for count, journal in enumerate(tqdm(journals, desc="Processing journals"), start=1):
            image_url = self.get_image_from_bing(journal.journal_title)

            if image_url:
                self.save_journal_image(journal, image_url)
            else:
                logging.info(f"No image found for journal: {journal.journal_title}")
                self.stdout.write(self.style.WARNING(f"No image found for journal: {journal.journal_title}"))

            self.stdout.write(self.style.SUCCESS(f"Processed journal: {journal.journal_title}"))

            if count >= 100:
                self.stdout.write(self.style.SUCCESS("Terminating after processing 100 journals."))
                break

    def get_image_from_bing(self, journal_title):
        """Use Bing Image Downloader to fetch the first image URL for a given journal title."""
        try:
            # Download images to a temporary directory
            download(journal_title, limit=1, output_dir='temp_images', adult_filter_off=True, force_replace=False, timeout=60)
            temp_dir = f'temp_images/{journal_title}'
            files = os.listdir(temp_dir)

            if files:
                # Return the path of the first downloaded image
                return os.path.join(temp_dir, files[0])
            logging.warning(f"No images found for journal: {journal_title}")
            return None
        except Exception as e:
            logging.error(f"Error fetching image for {journal_title}: {e}")
            return None

    def save_journal_image(self, journal, image_path):
        """Save an image file from the local path to the database."""
        try:
            with open(image_path, 'rb') as img_file:
                image_name = os.path.basename(image_path)
                image_file = BytesIO(img_file.read())

                # Save image to the database
                journal_image, created = JournalImage.objects.update_or_create(
                    journal=journal,
                    defaults={'description': f"Image for {journal.journal_title} from Bing"},
                )

                journal_image.image.save(image_name, File(image_file), save=True)
                logging.info(f"Image saved for journal: {journal.journal_title}")
                self.stdout.write(self.style.SUCCESS(f"Image saved for journal: {journal.journal_title}"))

            # Cleanup the temporary image file and directory
            os.remove(image_path)
            os.rmdir(os.path.dirname(image_path))

        except Exception as e:
            logging.error(f"Error saving image for journal {journal.journal_title}: {e}")
            self.stdout.write(self.style.ERROR(f"Error saving image for journal {journal.journal_title}: {e}"))
