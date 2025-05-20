from django.core.management.base import BaseCommand
from journalApis.models import Article

class Command(BaseCommand):
    help = "Update the journal field in the Article model using the Volume field row by row"

    def handle(self, *args, **kwargs):
        articles_to_update = Article.objects.filter(journal__isnull=True, volume__isnull=False)

        if not articles_to_update.exists():
            self.stdout.write(self.style.WARNING("No articles need updating."))
            return

        updated_count = 0

        for article in articles_to_update.iterator():  # Using iterator() for memory efficiency
            if article.volume and article.volume.journal:
                article.journal = article.volume.journal  # Assign journal from volume
                article.save(update_fields=['journal'])  # Update only the journal field
                updated_count += 1
                self.stdout.write(f"Updated Article ID {article.id} with Journal: {article.journal}")

        self.stdout.write(self.style.SUCCESS(f"Successfully updated {updated_count} articles."))
