# from django.core.management.base import BaseCommand
# from scholarly import scholarly
# from journalApis.models import Journal, Article
# from django.utils.timezone import now

# class Command(BaseCommand):
#     help = "Fetch articles using Scholarly and save them to the database for journals without articles."

#     def handle(self, *args, **kwargs):
#         # Query journals without articles
#         journals_without_articles = Journal.objects.filter(
#             articles__isnull=True
#         )

#         if not journals_without_articles.exists():
#             self.stdout.write(self.style.WARNING("No journals found without articles."))
#             return

#         # Iterate over all journals without articles
#         for journal in journals_without_articles:
#             self.stdout.write(self.style.NOTICE(f"Processing journal: {journal.journal_title}"))

#             # List to hold articles for bulk creation
#             articles = []

#             try:
#                 # Search for articles using Scholarly
#                 search_query = scholarly.search_pubs(journal.journal_title)

#                 # Fetch up to 10 articles
#                 for i, article in enumerate(search_query):
#                     try:
#                         # Extract metadata from Scholarly results
#                         title = article['bib']['title']
#                         authors = ", ".join(article['bib']['author'])
#                         publication_year = article['bib'].get('pub_year', None)
#                         abstract = article['bib'].get('abstract', 'No abstract available.')
#                         url = article.get('eprint_url', None)
#                         doi = article['bib'].get('doi', None)
#                         citation_count = article.get('num_citations', 0)
#                         reference_count = article.get('num_references', 0)

#                         # Set publication date based on the year if available
#                         if publication_year:
#                             publication_date = f"{publication_year}-01-01"  # Approximate publication date
#                         else:
#                             publication_date = None  # Leave as None if no year is available

#                         # Prepare the article for bulk creation
#                         articles.append(Article(
#                             journal=journal,
#                             title=title,
#                             authors=authors,
#                             abstract=abstract,
#                             publication_date=publication_date,
#                             url=url,
#                             doi=doi,
#                             citation_count=citation_count,
#                             reference_count=reference_count,
#                         ))

#                         # Limit to 10 articles per journal
#                         if len(articles) >= 10:
#                             break
#                     except Exception as article_error:
#                         self.stdout.write(self.style.ERROR(f"Error processing article: {article_error}"))
#                         continue

#                 # Bulk create articles
#                 if articles:
#                     Article.objects.bulk_create(articles)
#                     self.stdout.write(self.style.SUCCESS(
#                         f"Added {len(articles)} articles for journal: {journal.journal_title}"
#                     ))
#                 else:
#                     self.stdout.write(self.style.WARNING(f"No articles found for journal: {journal.journal_title}"))

#             except Exception as e:
#                 self.stdout.write(self.style.ERROR(
#                     f"Error processing journal {journal.journal_title}: {e}"
#                 ))

#         self.stdout.write(self.style.SUCCESS("Finished processing all journals without articles."))

'''
import time
import random
from django.core.management.base import BaseCommand
from scholarly import scholarly
from journalApis.models import Journal, Article
from django.utils.timezone import now

class Command(BaseCommand):
    help = "Fetch articles using Scholarly and save them to the database for journals without articles."

    # Configurable delay parameters
    BASE_DELAY = 5       # Base delay in seconds
    RANDOM_DELAY = 3     # Random additional delay to mimic human behavior

    def handle(self, *args, **kwargs):
        # Query journals without articles
        journals_without_articles = Journal.objects.filter(
            articles__isnull=True
        )

        if not journals_without_articles.exists():
            self.stdout.write(self.style.WARNING("No journals found without articles."))
            return

        # Iterate over all journals without articles
        for journal in journals_without_articles:
            self.stdout.write(self.style.NOTICE(f"Processing journal: {journal.journal_title}"))

            # List to hold articles for bulk creation
            articles = []

            try:
                # Search for articles using Scholarly
                search_query = scholarly.search_pubs(journal.journal_title)

                # Fetch up to 10 articles
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

                        # Set publication date based on the year if available
                        if publication_year:
                            publication_date = f"{publication_year}-01-01"  # Approximate publication date
                        else:
                            publication_date = None  # Leave as None if no year is available

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
                        self.stdout.write(self.style.ERROR(f"Error processing article: {article_error}"))
                        continue

                    # Introduce a randomized delay between requests to mimic human behavior
                    delay = self.BASE_DELAY + random.uniform(0, self.RANDOM_DELAY)
                    self.stdout.write(self.style.NOTICE(f"Delaying next article request by {delay:.2f} seconds..."))
                    time.sleep(delay)

                # Bulk create articles
                if articles:
                    Article.objects.bulk_create(articles)
                    self.stdout.write(self.style.SUCCESS(
                        f"Added {len(articles)} articles for journal: {journal.journal_title}"
                    ))
                else:
                    self.stdout.write(self.style.WARNING(f"No articles found for journal: {journal.journal_title}"))

            except Exception as e:
                self.stdout.write(self.style.ERROR(
                    f"Error processing journal {journal.journal_title}: {e}"
                ))

            # Randomized delay between journals
            delay = self.BASE_DELAY + random.uniform(0, self.RANDOM_DELAY)
            self.stdout.write(self.style.NOTICE(f"Delaying next journal request by {delay:.2f} seconds..."))
            time.sleep(delay)

        self.stdout.write(self.style.SUCCESS("Finished processing all journals without articles."))
'''

import time
import random
from django.core.management.base import BaseCommand
from scholarly import scholarly
from journalApis.models import Journal, Article
from django.utils.timezone import now


class Command(BaseCommand):
    help = "Fetch articles using Scholarly and save them to the database for journals without articles."

    # Configurable delay parameters
    BASE_DELAY = 5       # Base delay in seconds
    RANDOM_DELAY = 3     # Random additional delay to mimic human behavior

    def handle(self, *args, **kwargs):
        # Query journals without articles
        journals_without_articles = Journal.objects.filter(
            articles__isnull=True
        )

        if not journals_without_articles.exists():
            self.stdout.write(self.style.WARNING("No journals found without articles."))
            return

        # Iterate over all journals without articles
        for journal in journals_without_articles:
            self.stdout.write(self.style.NOTICE(f"Processing journal: {journal.journal_title}"))

            # List to hold articles for bulk creation
            articles = []

            try:
                # Search for articles using Scholarly
                search_query = scholarly.search_pubs(journal.journal_title)

                # Fetch up to 10 articles
                for i, article in enumerate(search_query):
                    try:
                        # Extract metadata from Scholarly results
                        title = article['bib']['title']
                        authors = ", ".join(article['bib']['author'])
                        publication_year = article['bib'].get('pub_year', None)
                        publication_month = article['bib'].get('pub_month', None)
                        publication_day = article['bib'].get('pub_day', None)
                        abstract = article['bib'].get('abstract', 'No abstract available.')
                        url = article.get('eprint_url', None)
                        doi = article['bib'].get('doi', None)
                        citation_count = article.get('num_citations', 0)
                        reference_count = article.get('num_references', 0)

                        # Validate and format the publication date dynamically
                        publication_date = None
                        try:
                            if publication_year and publication_year.isdigit():
                                year = int(publication_year)
                                month = int(publication_month) if publication_month and publication_month.isdigit() else 1
                                day = int(publication_day) if publication_day and publication_day.isdigit() else 1
                                publication_date = f"{year:04d}-{month:02d}-{day:02d}"
                        except ValueError:
                            self.stdout.write(self.style.ERROR(
                                f"Invalid date components (year: {publication_year}, month: {publication_month}, day: {publication_day})."
                            ))
                            publication_date = None

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
                        self.stdout.write(self.style.ERROR(f"Error processing article: {article_error}"))
                        continue

                    # Introduce a randomized delay between requests to mimic human behavior
                    delay = self.BASE_DELAY + random.uniform(0, self.RANDOM_DELAY)
                    self.stdout.write(self.style.NOTICE(f"Delaying next article request by {delay:.2f} seconds..."))
                    time.sleep(delay)

                # Bulk create articles
                if articles:
                    Article.objects.bulk_create(articles)
                    self.stdout.write(self.style.SUCCESS(
                        f"Added {len(articles)} articles for journal: {journal.journal_title}"
                    ))
                else:
                    self.stdout.write(self.style.WARNING(f"No articles found for journal: {journal.journal_title}"))

            except Exception as e:
                self.stdout.write(self.style.ERROR(
                    f"Error processing journal {journal.journal_title}: {e}"
                ))

            # Randomized delay between journals
            delay = self.BASE_DELAY + random.uniform(0, self.RANDOM_DELAY)
            self.stdout.write(self.style.NOTICE(f"Delaying next journal request by {delay:.2f} seconds..."))
            time.sleep(delay)

        self.stdout.write(self.style.SUCCESS("Finished processing all journals without articles."))
