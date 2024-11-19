
import requests
from django.core.management.base import BaseCommand
from journalApis.models import Journal, Volume, Article, LastProcessedJournal
import urllib.parse
from datetime import datetime
import time
from django.db import IntegrityError

class Command(BaseCommand):
    help = 'Fetches articles from CrossRef and populates the Volume and Article models.'

    def handle(self, *args, **kwargs):
        # Fetch the last processed journal
        last_processed = LastProcessedJournal.objects.first()
        last_processed_id = last_processed.last_processed_id if last_processed else 0

        # Fetch all journals after the last processed one
        journals = Journal.objects.filter(id__gt=last_processed_id)

        # Define the rate limit (e.g., 1 request per second)
        rate_limit_delay = 1  # 1 second delay between API calls
        max_requests_per_minute = 60  # Adjust this value based on the API's rate limit

        request_count = 0  # To track the number of requests made in the current period

        for journal in journals:
            journal_title = journal.journal_title
            print(f"Processing journal: {journal_title}")

            # URL encode the journal title to ensure it's valid for use in the URL
            encoded_title = urllib.parse.quote(journal_title)

            # CrossRef API URL for journal article search with the 'container-title' filter
            url = f"https://api.crossref.org/works?filter=container-title:{encoded_title}"

            # Send request to CrossRef API
            response = requests.get(url)

            if response.status_code == 200:
                data = response.json()
                items = data.get('message', {}).get('items', [])

                if not items:
                    print(f"No articles found for journal: {journal_title}")
                else:
                    # Iterate over the articles and process each
                    for item in items:
                        # Check if the article has a title before proceeding
                        title = item.get("title", [""])[0]
                        if not title:  # Skip if title is empty
                            print(f"Skipping article without title for journal: {journal_title}")
                            continue  # Skip this article

                        volume_number = item.get("volume")
                        issue_number = item.get("issue")

                        # Sanitize issue_number to ensure it's an integer or None
                        if issue_number:
                            try:
                                issue_number = int(''.join(filter(str.isdigit, str(issue_number))))  # Extract numeric part
                            except ValueError:
                                issue_number = None  # If it can't be converted, set to None
                        
                        # Extract and parse the published date
                        date_parts = item.get("published", {}).get("date-parts", [[None]])[0]
                        published_date = None

                        if date_parts:
                            try:
                                if len(date_parts) == 1:
                                    # Only the year is available
                                    published_date = datetime(date_parts[0], 1, 1).date()
                                elif len(date_parts) == 2:
                                    # Year and month are available
                                    published_date = datetime(date_parts[0], date_parts[1], 1).date()
                                elif len(date_parts) == 3:
                                    # Full date is available
                                    published_date = datetime(date_parts[0], date_parts[1], date_parts[2]).date()
                            except ValueError:
                                published_date = None

                        # Check if volume already exists
                        existing_volume = Volume.objects.filter(
                            journal=journal,
                            volume_number=volume_number if volume_number else 0,  # Default to 0 if missing
                            issue_number=issue_number if issue_number else 1,  # Default to 1 if missing
                        ).first()

                        if existing_volume:
                            print(f"Volume {volume_number}, issue {issue_number} already exists for journal: {journal_title}")
                        else:
                            # If the volume doesn't exist, create it
                            try:
                                volume = Volume.objects.create(
                                    journal=journal,
                                    volume_number=volume_number if volume_number else 0,
                                    issue_number=issue_number if issue_number else 1,
                                    year=published_date.year if published_date else None
                                )
                                print(f"Created volume: {volume_number}, issue: {issue_number}")
                            except IntegrityError:
                                print(f"Volume {volume_number}, issue {issue_number} already exists (IntegrityError)")
                                continue

                        # Prepare author names
                        authors = item.get("author", [])
                        author_names = ", ".join(
                            [f"{author.get('given', '')} {author.get('family', '')}" for author in authors]
                        ) if authors else "No authors"

                        # Additional metadata for the article
                        doi = item.get("DOI", "No DOI")
                        article_url = item.get("URL", "No URL")
                        reference_count = item.get("reference-count", 0)
                        citation_count = item.get("is-referenced-by-count", 0)
                        license_url = item.get("license", [{}])[0].get("URL", "No license URL")
                        page_start = item.get("page", "").split("-")[0] if item.get("page") else None
                        page_end = item.get("page", "").split("-")[1] if item.get("page") and "-" in item.get("page") else None
                        abstract = item.get("abstract", "No abstract")
                        article_type = item.get("type", "No type")
                        issn_electronic = item.get("ISSN", [None])[0] if item.get("ISSN") else None
                        issn_print = item.get("ISSN", [None, None])[1] if len(item.get("ISSN", [])) > 1 else None
                        publisher = item.get("publisher", "No publisher")
                        publisher_location = item.get("publisher-location", "No publisher location")

                        # Create or get the article instance
                        article, article_created = Article.objects.get_or_create(
                            title=title,
                            volume=existing_volume if existing_volume else volume,
                            authors=author_names,
                            publication_date=published_date,
                            doi=doi,
                            url=article_url,
                            reference_count=reference_count,
                            citation_count=citation_count,
                            license_url=license_url,
                            page_start=page_start,
                            page_end=page_end,
                            abstract=abstract,
                            subjects=", ".join(item.get("subject", [])),  # Comma-separated subjects
                            article_type=article_type,
                            electronic_issn=issn_electronic,
                            print_issn=issn_print,
                            publisher=publisher,
                            publisher_location=publisher_location
                        )

                        if article_created:
                            print(f"Created article: {title}")
                        else:
                            print(f"Article already exists: {title}")
                        
                        # Rate limiting - Add a delay to avoid hitting API too frequently
                        request_count += 1
                        if request_count >= max_requests_per_minute:
                            print("Rate limit reached, pausing for a minute...")
                            time.sleep(60)  # Wait for a minute before making more requests
                            request_count = 0  # Reset the count after the pause

            else:
                print(f"Failed to retrieve data for {journal_title}: {response.status_code}")
            
            # Update the last processed journal ID
            LastProcessedJournal.objects.update_or_create(
                defaults={"last_processed_id": journal.id}
            )

            # General rate limiting - Add a small delay between requests to avoid too frequent calls
            print(f"Pausing for {rate_limit_delay} seconds...")
            time.sleep(rate_limit_delay)
