'''
import time
import random
import logging
from django.core.management.base import BaseCommand
from scholarly import scholarly
from journalApis.models import Journal, Article

# Configure logging
logging.basicConfig(
    filename='scholarly_fetch.log',  # Log file name
    level=logging.INFO,             # Log level
    format='%(asctime)s - %(levelname)s - %(message)s'  # Log format
)

class Command(BaseCommand):
    help = "Fetch articles using Scholarly and save them to the database for journals without volumes or articles."

    # Configurable delay parameters
    BASE_DELAY = 10      # Base delay in seconds between requests
    RANDOM_DELAY = 5      # Random additional delay to mimic human behavior
    MAX_RETRIES = 3       # Maximum retries if a query fails

    def handle(self, *args, **kwargs):
        # Filter journals without volumes or articles and order by ID
        journals_to_process = Journal.objects.filter(
            volumes__isnull=True,
            articles__isnull=True
        ).order_by('id')  # Process journals by ascending ID

        if not journals_to_process.exists():
            message = "No journals found without volumes or articles."
            self.stdout.write(self.style.WARNING(message))
            logging.warning(message)
            return

        for journal in journals_to_process:
            message = f"Processing journal: {journal.journal_title}"
            self.stdout.write(self.style.NOTICE(message))
            logging.info(message)

            articles = []

            try:
                # Fetch articles with retry logic
                search_query = self.fetch_with_rate_limiting(journal.journal_title)

                for i, article in enumerate(search_query):
                    try:
                        # Extract metadata from Scholarly results
                        title = article['bib']['title']
                        authors = ", ".join(article['bib']['author'])
                        publication_year = article['bib'].get('pub_year', None)
                        abstract = article['bib'].get('abstract', 'No abstract available.')
                        url = article.get('eprint_url', None)
                        doi = article['bib'].get('doi', None)
                        citation_count = article.get('num_citations', 0)
                        reference_count = article.get('num_references', 0)

                        # Format publication date
                        publication_date = None
                        if publication_year and publication_year.isdigit():
                            publication_date = f"{publication_year}-01-01"

                        # Prepare the article for bulk creation
                        articles.append(Article(
                            journal=journal,
                            title=title,
                            authors=authors,
                            abstract=abstract,
                            publication_date=publication_date,
                            url=url,
                            doi=doi,
                            citation_count=citation_count,
                            reference_count=reference_count,
                        ))

                        # Limit to 10 articles per journal
                        if len(articles) >= 10:
                            break

                    except Exception as article_error:
                        error_message = f"Error processing article: {article_error}"
                        self.stdout.write(self.style.ERROR(error_message))
                        logging.error(error_message)
                        continue

                    # Randomized delay between article requests
                    delay = self.BASE_DELAY + random.uniform(0, self.RANDOM_DELAY)
                    delay_message = f"Delaying next article request by {delay:.2f} seconds..."
                    self.stdout.write(self.style.NOTICE(delay_message))
                    logging.info(delay_message)
                    time.sleep(delay)

                # Bulk create articles
                if articles:
                    Article.objects.bulk_create(articles)
                    success_message = f"Added {len(articles)} articles for journal: {journal.journal_title}"
                    self.stdout.write(self.style.SUCCESS(success_message))
                    logging.info(success_message)
                else:
                    warning_message = f"No articles found for journal: {journal.journal_title}"
                    self.stdout.write(self.style.WARNING(warning_message))
                    logging.warning(warning_message)

            except Exception as e:
                error_message = f"Error processing journal {journal.journal_title}: {e}. Skipping."
                self.stdout.write(self.style.ERROR(error_message))
                logging.error(error_message)
                continue

            # Delay between journals
            delay = self.BASE_DELAY + random.uniform(0, self.RANDOM_DELAY)
            delay_message = f"Delaying next journal request by {delay:.2f} seconds..."
            self.stdout.write(self.style.NOTICE(delay_message))
            logging.info(delay_message)
            time.sleep(delay)

        completion_message = "Finished processing all journals without volumes or articles."
        self.stdout.write(self.style.SUCCESS(completion_message))
        logging.info(completion_message)

    def fetch_with_rate_limiting(self, journal_title):
        """
        Fetch articles with rate limiting and retry logic.
        """
        retries = 0
        while retries < self.MAX_RETRIES:
            try:
                message = f"Querying Scholarly for journal: {journal_title} (Attempt {retries + 1})"
                self.stdout.write(self.style.NOTICE(message))
                logging.info(message)
                search_query = scholarly.search_pubs(journal_title)
                return search_query
            except Exception as e:
                retries += 1
                delay = self.BASE_DELAY + random.uniform(0, self.RANDOM_DELAY)
                error_message = f"Error querying Scholarly: {e}. Retrying after {delay:.2f} seconds..."
                self.stdout.write(self.style.ERROR(error_message))
                logging.error(error_message)
                time.sleep(delay)
        raise Exception("Failed to fetch data after maximum retries.")
'''

import random
import logging
import time
from django.core.management.base import BaseCommand
from scholarly import scholarly
from journalApis.models import Journal, Article
import requests

# Configure logging
logging.basicConfig(
    filename='scholarly_fetch.log',  # Log file name
    level=logging.INFO,             # Log level
    format='%(asctime)s - %(levelname)s - %(message)s'  # Log format
)

class Command(BaseCommand):
    help = "Fetch articles using Scholarly and save them to the database for journals without volumes or articles."

    # Configurable delay parameters
    BASE_DELAY = 10      # Base delay in seconds between requests
    RANDOM_DELAY = 5      # Random additional delay to mimic human behavior
    MAX_RETRIES = 3       # Maximum retries if a query fails

    def handle(self, *args, **kwargs):
        # Set up User-Agent and Proxy for scholarly
        self.set_user_agent()

        # Filter journals without volumes or articles and order by ID
        journals_to_process = Journal.objects.filter(
            volumes__isnull=True,
            articles__isnull=True
        ).order_by('id')  # Process journals by ascending ID

        if not journals_to_process.exists():
            message = "No journals found without volumes or articles."
            self.stdout.write(self.style.WARNING(message))
            logging.warning(message)
            return

        for journal in journals_to_process:
            message = f"Processing journal: {journal.journal_title}"
            self.stdout.write(self.style.NOTICE(message))
            logging.info(message)

            articles = []

            try:
                # Fetch articles with retry logic
                search_query = self.fetch_with_rate_limiting(journal.journal_title)

                for i, article in enumerate(search_query):
                    try:
                        # Extract metadata from Scholarly results
                        title = article['bib']['title']
                        authors = ", ".join(article['bib']['author'])
                        publication_year = article['bib'].get('pub_year', None)
                        abstract = article['bib'].get('abstract', 'No abstract available.')
                        url = article.get('eprint_url', None)
                        doi = article['bib'].get('doi', None)
                        citation_count = article.get('num_citations', 0)
                        reference_count = article.get('num_references', 0)

                        # Format publication date
                        publication_date = None
                        if publication_year and publication_year.isdigit():
                            publication_date = f"{publication_year}-01-01"

                        # Prepare the article for bulk creation
                        articles.append(Article(
                            journal=journal,
                            title=title,
                            authors=authors,
                            abstract=abstract,
                            publication_date=publication_date,
                            url=url,
                            doi=doi,
                            citation_count=citation_count,
                            reference_count=reference_count,
                        ))

                        # Limit to 10 articles per journal
                        if len(articles) >= 10:
                            break

                    except Exception as article_error:
                        error_message = f"Error processing article: {article_error}"
                        self.stdout.write(self.style.ERROR(error_message))
                        logging.error(error_message)
                        continue

                    # Randomized delay between article requests
                    delay = self.BASE_DELAY + random.uniform(0, self.RANDOM_DELAY)
                    delay_message = f"Delaying next article request by {delay:.2f} seconds..."
                    self.stdout.write(self.style.NOTICE(delay_message))
                    logging.info(delay_message)
                    time.sleep(delay)

                # Bulk create articles
                if articles:
                    Article.objects.bulk_create(articles)
                    success_message = f"Added {len(articles)} articles for journal: {journal.journal_title}"
                    self.stdout.write(self.style.SUCCESS(success_message))
                    logging.info(success_message)
                else:
                    warning_message = f"No articles found for journal: {journal.journal_title}"
                    self.stdout.write(self.style.WARNING(warning_message))
                    logging.warning(warning_message)

            except Exception as e:
                error_message = f"Error processing journal {journal.journal_title}: {e}. Skipping."
                self.stdout.write(self.style.ERROR(error_message))
                logging.error(error_message)
                continue

            # Delay between journals
            delay = self.BASE_DELAY + random.uniform(0, self.RANDOM_DELAY)
            delay_message = f"Delaying next journal request by {delay:.2f} seconds..."
            self.stdout.write(self.style.NOTICE(delay_message))
            logging.info(delay_message)
            time.sleep(delay)

        completion_message = "Finished processing all journals without volumes or articles."
        self.stdout.write(self.style.SUCCESS(completion_message))
        logging.info(completion_message)

    def fetch_with_rate_limiting(self, journal_title):
        """
        Fetch articles with rate limiting and retry logic.
        Detect and log CAPTCHA requests for manual resolution.
        """
        retries = 0
        while retries < self.MAX_RETRIES:
            try:
                message = f"Querying Scholarly for journal: {journal_title} (Attempt {retries + 1})"
                self.stdout.write(self.style.NOTICE(message))
                logging.info(message)

                # Perform the search query
                search_query = scholarly.search_pubs(journal_title)

                # Check if CAPTCHA page is returned
                if "captcha" in str(search_query):
                    captcha_message = f"CAPTCHA detected while querying Scholarly for journal: {journal_title}. Please resolve manually."
                    self.stdout.write(self.style.ERROR(captcha_message))
                    logging.error(captcha_message)

                    # Handle CAPTCHA resolution process
                    while "captcha" in str(search_query):
                        self.stdout.write(self.style.NOTICE("Waiting for CAPTCHA resolution..."))
                        time.sleep(10)  # Increase waiting time before retrying
                        search_query = scholarly.search_pubs(journal_title)  # Retry search after waiting

                return search_query

            except Exception as e:
                # Handle other errors (e.g., network issues, rate-limiting)
                error_message = f"Error querying Scholarly: {e}. Retrying..."
                self.stdout.write(self.style.ERROR(error_message))
                logging.error(error_message)
                retries += 1
                delay = self.BASE_DELAY + random.uniform(0, self.RANDOM_DELAY)
                time.sleep(delay)

        raise Exception("Failed to fetch data after maximum retries.")

    def set_user_agent(self):
        """
        Configure Scholarly to use a custom User-Agent header.
        """
        # Set the User-Agent globally for requests made by Scholarly
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                          "AppleWebKit/537.36 (KHTML, like Gecko) "
                          "Chrome/113.0.0.0 Safari/537.36"
        }
        # Use the requests library to set the global User-Agent header
        requests.Session().headers.update(headers)
