from django.core.management.base import BaseCommand
from journalApis.models import Journal  # update 'journals' to match your actual app name


class Command(BaseCommand):
    help = 'Mark all journals as approved'

    def add_arguments(self, parser):
        parser.add_argument(
            '--dry-run',
            action='store_true',
            help='Preview how many journals will be updated without making changes',
        )

    def handle(self, *args, **options):
        dry_run = options['dry_run']

        unapproved = Journal.objects.filter(approved=False)
        count = unapproved.count()

        if count == 0:
            self.stdout.write(self.style.SUCCESS('All journals are already approved. Nothing to update.'))
            return

        if dry_run:
            self.stdout.write(self.style.WARNING(f'[Dry Run] {count} journal(s) would be marked as approved.'))
            return

        updated = unapproved.update(approved=True)
        self.stdout.write(self.style.SUCCESS(f'Successfully approved {updated} journal(s).'))