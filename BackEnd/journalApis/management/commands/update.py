import pandas as pd
from django.core.management.base import BaseCommand
from journalApis.models import Language, Platform, Country, ThematicArea, Journal

class Command(BaseCommand):
    help = 'Update existing data from an Excel file into the database, maintaining index order.'

    def add_arguments(self, parser):
        parser.add_argument('excel_file_path', type=str, help='Path to the Excel file to be loaded.')

    def handle(self, *args, **kwargs):
        excel_file_path = kwargs['excel_file_path']

        # Load the Excel spreadsheet
        df = pd.read_excel(excel_file_path)
        self.stdout.write(self.style.SUCCESS(f"Loaded {df.shape[0]} rows from the Excel file."))

        # Fetch all journals in the order they were inserted
        journals = list(Journal.objects.all().order_by('id'))  # Assuming ID reflects insertion order

        if len(df) < len(journals):
            self.stdout.write(self.style.WARNING(f"Excel has fewer records ({len(df)}) than the database ({len(journals)}). Some database records will not be updated."))

        # Iterate over both the database records and DataFrame rows simultaneously
        for index, (journal, row) in enumerate(zip(journals, df.itertuples(index=False))):
            try:
                journal.language = self.get_model_instance(Language, 'language', getattr(row, 'Language', None))
                journal.platform = self.get_model_instance(Platform, 'platform', getattr(row, 'Platform', None))
                journal.country = self.get_model_instance(Country, 'country', getattr(row, 'Country', None))
                journal.thematic_area = self.get_model_instance(ThematicArea, 'thematic_area', getattr(row, 'Thematic area', None))

                journal.journal_title = getattr(row, 'Journal_title', '').strip()
                journal.publishers_name = getattr(row, 'Publishers Name', None)
                journal.link = getattr(row, 'Link', None)
                journal.aim_identifier = self.convert_to_boolean(getattr(row, 'African Index Medicus', None))
                journal.medline = self.convert_to_boolean(getattr(row, 'Medline (Medicine and Health Journals)', None))
                journal.google_scholar_index = self.convert_to_boolean(getattr(row, 'Indexed on Google Scholar', None))
                journal.impact_factor = self.convert_to_float(getattr(row, 'Impact Factor', None))
                journal.sjr = self.convert_to_boolean(getattr(row, 'Scimago Jornal and Country Rank (SJR); Scopus', None))
                journal.h_index = self.convert_to_float(getattr(row, 'H-Index', None))
                journal.eigen_factor = self.convert_to_boolean(getattr(row, 'Eigenfactor ', None))
                journal.eigen_metrix = getattr(row, 'Eigenfactor metrix', None)
                journal.snip = self.convert_to_boolean(getattr(row, 'Source Normalized Impact per Paper (SNIP)', None))
                journal.snip_metrix = self.convert_to_float(getattr(row, 'SNIP metrix', None))
                journal.open_access_journal = self.convert_to_boolean(getattr(row, 'Open Access Journal', None))
                journal.listed_in_doaj = self.convert_to_boolean(getattr(row, 'Journal listed in the Directory of Open Access (DOAJ)', None))
                journal.present_issn = self.convert_to_boolean(getattr(row, 'Present on International Standard Serial Number (ISSN) portal', None))
                journal.publisher_in_cope = self.convert_to_boolean(getattr(row, 'The publisher is a member of Committee on publication Ethics (COPE)', None))
                journal.online_publisher_africa = self.convert_to_boolean(getattr(row, 'Online publisher based in Africa', None))
                journal.hosted_on_inasps = self.convert_to_boolean(getattr(row, "Hosted on INASP'S Journal online", None))
                journal.summary = getattr(row, 'Summary', None)

                # Save the updated journal record
                journal.save()
                self.stdout.write(self.style.SUCCESS(f"Updated record {index}: {journal.journal_title}"))

            except Exception as e:
                self.stdout.write(self.style.ERROR(f"Error updating record {index}: {e}"))

        self.stdout.write(self.style.SUCCESS('Database successfully updated in sequential order.'))

    def get_model_instance(self, model_class, field_name, value):
        """Helper function to get model instance if it exists."""
        if pd.notna(value):
            try:
                return model_class.objects.get(**{field_name: value})
            except model_class.DoesNotExist:
                return None
        return None

    def convert_to_boolean(self, value):
        """Convert boolean-like values."""
        if pd.isna(value):
            return None
        value = str(value).strip().lower()
        return value in ['true', '1', 'yes', 'y']

    def convert_to_float(self, value):
        """Convert to float, handling errors."""
        try:
            return float(value) if pd.notna(value) else None
        except (ValueError, TypeError):
            return None
