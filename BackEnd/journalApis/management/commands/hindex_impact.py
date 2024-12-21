# import google.generativeai as genai
# import logging
# import time
# import os
# from django.core.management.base import BaseCommand
# from journalApis.models import Journal

# # Configure Google Generative AI
# genai.configure(api_key='AIzaSyAOzFi1cTqFQIMF8aScgh58r6R0QQ_zii0')
# model = genai.GenerativeModel("gemini-1.5-flash")

# # Configure logging
# logging.basicConfig(
#     filename="fetch_journal_metrics.log",
#     level=logging.INFO,
#     format="%(asctime)s - %(levelname)s - %(message)s",
# )

# # Progress file
# PROGRESS_FILE = "progress.txt"


# class Command(BaseCommand):
#     help = "Fetch Impact Factor and h-index for journals from Gemini API and update the database only if fields are null."

#     def handle(self, *args, **kwargs):
#         # Get the last processed ID from progress.txt
#         last_processed_id = self.get_last_processed_id()

#         # Fetch journals starting from the last processed ID
#         journals = (
#             Journal.objects.filter(impact_factor__isnull=True) |
#             Journal.objects.filter(h_index__isnull=True)
#         ).order_by("id")

#         if last_processed_id is not None:
#             journals = journals.filter(id__gt=last_processed_id)

#         if not journals.exists():
#             logging.info("No journals found with null Impact Factor or H-index.")
#             self.stdout.write(self.style.NOTICE("No journals found to update."))
#             return

#         logging.info(f"Starting to process {journals.count()} journals...")

#         for index, journal in enumerate(journals, start=1):
#             journal_title = journal.journal_title

#             # Prepare prompt
#             prompt = f"What is the 2022 Impact Factor and h-index of the journal '{journal_title}'? Just return the float numbers separated by a comma and avoid explanations."

#             try:
#                 # Query Gemini API
#                 logging.info(f"Fetching data for journal: {journal_title} (Journal {index}/{journals.count()})")
#                 response = model.generate_content(prompt)

#                 # Parse response
#                 if response and response.text:
#                     values = response.text.strip().split(",")
#                     if len(values) == 2:
#                         # Extract values
#                         impact_factor = float(values[0].strip())
#                         h_index = int(values[1].strip())

#                         # Update fields only if null
#                         updated = False
#                         if journal.impact_factor is None:
#                             journal.impact_factor = impact_factor
#                             updated = True
#                         if journal.h_index is None:
#                             journal.h_index = h_index
#                             updated = True

#                         if updated:
#                             journal.save()
#                             msg = f"Updated: {journal_title} -> IF: {journal.impact_factor}, H-Index: {journal.h_index}"
#                             logging.info(msg)
#                             self.stdout.write(self.style.SUCCESS(msg))
#                         else:
#                             msg = f"No update needed for: {journal_title}"
#                             logging.info(msg)
#                             self.stdout.write(self.style.NOTICE(msg))
#                     else:
#                         msg = f"Unexpected format for {journal_title}: {response.text}"
#                         logging.warning(msg)
#                         self.stdout.write(self.style.WARNING(msg))
#                 else:
#                     msg = f"No response for {journal_title}"
#                     logging.warning(msg)
#                     self.stdout.write(self.style.WARNING(msg))

#                 # Save progress to file
#                 self.save_progress(journal.id)

#                 # Enforce rate limiting (1 second delay between API calls)
#                 time.sleep(1)

#             except Exception as e:
#                 error_msg = f"Error processing {journal_title}: {str(e)}"
#                 logging.error(error_msg)
#                 self.stdout.write(self.style.ERROR(error_msg))
#                 break  # Stop processing on error

#         logging.info("Finished processing journals.")
#         self.stdout.write(self.style.SUCCESS("Completed processing all journals."))

#     def get_last_processed_id(self):
#         """
#         Reads the last processed journal ID from the progress file.
#         Returns None if the file doesn't exist or is empty.
#         """
#         if os.path.exists(PROGRESS_FILE):
#             with open(PROGRESS_FILE, "r") as f:
#                 content = f.read().strip()
#                 if content.isdigit():
#                     return int(content)
#         return None

#     def save_progress(self, journal_id):
#         """
#         Saves the current journal ID to the progress file.
#         """
#         with open(PROGRESS_FILE, "w") as f:
#             f.write(str(journal_id))
#         logging.info(f"Progress saved: Last processed journal ID = {journal_id}")

'''
import google.generativeai as genai
import logging
import time
import os
from django.core.management.base import BaseCommand
from journalApis.models import Journal

# Configure Google Generative AI
genai.configure(api_key='AIzaSyAOzFi1cTqFQIMF8aScgh58r6R0QQ_zii0')
model = genai.GenerativeModel("gemini-1.5-flash")

# Configure logging
logging.basicConfig(
    filename="fetch_journal_metrics.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
)

# Progress file
PROGRESS_FILE = "progress.txt"

# Rate limit parameters
RATE_LIMIT_DELAY = 5  # seconds between API calls
MAX_RETRIES = 3  # maximum number of retries per call


class Command(BaseCommand):
    help = "Fetch Impact Factor and h-index for journals from Gemini API and update the database only if fields are null."

    def handle(self, *args, **kwargs):
        # Get the last processed ID from progress.txt
        last_processed_id = self.get_last_processed_id()

        # Fetch journals starting from the last processed ID
        journals = (
            Journal.objects.filter(impact_factor__isnull=True) |
            Journal.objects.filter(h_index__isnull=True)
        ).order_by("id")

        if last_processed_id is not None:
            journals = journals.filter(id__gt=last_processed_id)

        if not journals.exists():
            logging.info("No journals found with null Impact Factor or H-index.")
            self.stdout.write(self.style.NOTICE("No journals found to update."))
            return

        logging.info(f"Starting to process {journals.count()} journals...")

        for index, journal in enumerate(journals, start=1):
            journal_title = journal.journal_title

            # Prepare prompt
            prompt = f"What is the 2022 Impact Factor and h-index of the journal '{journal_title}'? Just return the float numbers separated by a comma and avoid explanations."

            retries = 0
            while retries < MAX_RETRIES:
                try:
                    # Query Gemini API
                    logging.info(f"Fetching data for journal: {journal_title} (Journal {index}/{journals.count()})")
                    response = model.generate_content(prompt)

                    # Parse response
                    if response and response.text:
                        values = response.text.strip().split(",")
                        if len(values) == 2:
                            # Extract values
                            impact_factor = float(values[0].strip())
                            h_index = int(values[1].strip())

                            # Update fields only if null
                            updated = False
                            if journal.impact_factor is None:
                                journal.impact_factor = impact_factor
                                updated = True
                            if journal.h_index is None:
                                journal.h_index = h_index
                                updated = True

                            if updated:
                                journal.save()
                                msg = f"Updated: {journal_title} -> IF: {journal.impact_factor}, H-Index: {journal.h_index}"
                                logging.info(msg)
                                self.stdout.write(self.style.SUCCESS(msg))
                            else:
                                msg = f"No update needed for: {journal_title}"
                                logging.info(msg)
                                self.stdout.write(self.style.NOTICE(msg))
                        else:
                            msg = f"Unexpected format for {journal_title}: {response.text}"
                            logging.warning(msg)
                            self.stdout.write(self.style.WARNING(msg))
                    else:
                        msg = f"No response for {journal_title}"
                        logging.warning(msg)
                        self.stdout.write(self.style.WARNING(msg))

                    # Save progress to file
                    self.save_progress(journal.id)

                    # Respect rate limits
                    time.sleep(RATE_LIMIT_DELAY)
                    break  # Exit retry loop if successful

                except Exception as e:
                    retries += 1
                    error_msg = f"Error processing {journal_title} on attempt {retries}: {str(e)}"
                    logging.error(error_msg)
                    self.stdout.write(self.style.ERROR(error_msg))

                    # Exponential backoff
                    time.sleep(RATE_LIMIT_DELAY * (2 ** retries))

            if retries == MAX_RETRIES:
                logging.error(f"Failed to process {journal_title} after {MAX_RETRIES} attempts.")
                break  # Stop processing if the maximum retries are reached

        logging.info("Finished processing journals.")
        self.stdout.write(self.style.SUCCESS("Completed processing all journals."))

    def get_last_processed_id(self):
        """
        Reads the last processed journal ID from the progress file.
        Returns None if the file doesn't exist or is empty.
        """
        if os.path.exists(PROGRESS_FILE):
            with open(PROGRESS_FILE, "r") as f:
                content = f.read().strip()
                if content.isdigit():
                    return int(content)
        return None

    def save_progress(self, journal_id):
        """
        Saves the current journal ID to the progress file.
        """
        with open(PROGRESS_FILE, "w") as f:
            f.write(str(journal_id))
        logging.info(f"Progress saved: Last processed journal ID = {journal_id}")
'''

import google.generativeai as genai
import logging
import time
import os
from django.core.management.base import BaseCommand
from journalApis.models import Journal

# Configure Google Generative AI
genai.configure(api_key='AIzaSyAOzFi1cTqFQIMF8aScgh58r6R0QQ_zii0')
model = genai.GenerativeModel("gemini-1.5-flash")

# Configure logging
logging.basicConfig(
    filename="fetch_journal_metrics.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
)

# Progress file
PROGRESS_FILE = "progress.txt"

# Rate limit parameters
RATE_LIMIT_DELAY = 5  # seconds between API calls
MAX_RETRIES = 3  # maximum number of retries per call


class Command(BaseCommand):
    help = "Fetch Impact Factor and h-index for journals from Gemini API and update the database only if fields are null."

    def handle(self, *args, **kwargs):
        # Get the last processed ID from progress.txt
        last_processed_id = self.get_last_processed_id()

        # Fetch journals starting from the last processed ID
        journals = (
            Journal.objects.filter(impact_factor__isnull=True) |
            Journal.objects.filter(h_index__isnull=True)
        ).order_by("id")

        if last_processed_id is not None:
            journals = journals.filter(id__gt=last_processed_id)

        if not journals.exists():
            logging.info("No journals found with null Impact Factor or H-index.")
            self.stdout.write(self.style.NOTICE("No journals found to update."))
            return

        logging.info(f"Starting to process {journals.count()} journals...")

        for index, journal in enumerate(journals, start=1):
            journal_title = journal.journal_title

            # Prepare prompt
            prompt = f"What is the 2022 Impact Factor and h-index of the journal '{journal_title}'? Just return the float numbers separated by a comma and avoid explanations."

            retries = 0
            while retries < MAX_RETRIES:
                try:
                    # Query Gemini API
                    logging.info(f"Fetching data for journal: {journal_title} (Journal {index}/{journals.count()})")
                    response = model.generate_content(prompt)

                    # Parse response
                    if response and response.text:
                        values = response.text.strip().split(",")
                        
                        # Validate response content
                        if len(values) == 2 and all(
                            v.strip().lower() not in {"no data available", "not applicable", "not available"} for v in values
                        ):
                            try:
                                # Attempt to convert values
                                impact_factor = float(values[0].strip())
                                h_index = int(values[1].strip())
                            except ValueError:
                                raise ValueError(f"Invalid numeric format in response: {response.text}")

                            # Update fields only if null
                            updated = False
                            if journal.impact_factor is None:
                                journal.impact_factor = impact_factor
                                updated = True
                            if journal.h_index is None:
                                journal.h_index = h_index
                                updated = True

                            if updated:
                                journal.save()
                                msg = f"Updated: {journal_title} -> IF: {journal.impact_factor}, H-Index: {journal.h_index}"
                                logging.info(msg)
                                self.stdout.write(self.style.SUCCESS(msg))
                            else:
                                msg = f"No update needed for: {journal_title}"
                                logging.info(msg)
                                self.stdout.write(self.style.NOTICE(msg))
                        else:
                            msg = f"Invalid data format or 'No data available' for {journal_title}: {response.text}"
                            logging.warning(msg)
                            self.stdout.write(self.style.WARNING(msg))

                    else:
                        msg = f"No response for {journal_title}"
                        logging.warning(msg)
                        self.stdout.write(self.style.WARNING(msg))

                    # Save progress to file
                    self.save_progress(journal.id)

                    # Respect rate limits
                    time.sleep(RATE_LIMIT_DELAY)
                    break  # Exit retry loop if successful

                except Exception as e:
                    retries += 1
                    error_msg = f"Error processing {journal_title} on attempt {retries}: {str(e)}"
                    logging.error(error_msg)
                    self.stdout.write(self.style.ERROR(error_msg))

                    # Exponential backoff
                    time.sleep(RATE_LIMIT_DELAY * (2 ** retries))

            if retries == MAX_RETRIES:
                logging.error(f"Skipping {journal_title} after {MAX_RETRIES} attempts.")
                self.stdout.write(self.style.WARNING(f"Skipping {journal_title} after {MAX_RETRIES} attempts."))

        logging.info("Finished processing journals.")
        self.stdout.write(self.style.SUCCESS("Completed processing all journals."))

    def get_last_processed_id(self):
        """
        Reads the last processed journal ID from the progress file.
        Returns None if the file doesn't exist or is empty.
        """
        if os.path.exists(PROGRESS_FILE):
            with open(PROGRESS_FILE, "r") as f:
                content = f.read().strip()
                if content.isdigit():
                    return int(content)
        return None

    def save_progress(self, journal_id):
        """
        Saves the current journal ID to the progress file.
        """
        with open(PROGRESS_FILE, "w") as f:
            f.write(str(journal_id))
        logging.info(f"Progress saved: Last processed journal ID = {journal_id}")
