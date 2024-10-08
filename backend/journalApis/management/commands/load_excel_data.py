#python manage.py load_excel_data "C:\Users\guest478\Downloads\visibility.xlsx"

import pandas as pd
from django.core.management.base import BaseCommand
from journalApis.models import Language, Platform, Country, ThematicArea, Journal

class Command(BaseCommand):
    help = 'Load data from an Excel file into the database.'

    def add_arguments(self, parser):
        parser.add_argument('excel_file_path', type=str, help='Path to the Excel file to be loaded.')

    def handle(self, *args, **kwargs):
        excel_file_path = kwargs['excel_file_path']

        # Load the Excel spreadsheet
        df = pd.read_excel(excel_file_path)
        self.stdout.write(self.style.SUCCESS(f"Loaded {df.shape[0]} rows from the Excel file."))

        # Iterate over the rows in the DataFrame
        for index, row in df.iterrows():
            try:
                aim_value = row.get('African Index Medicus')
                converted_aim = self.convert_to_boolean(aim_value)
                print(f"Row {index} - AIM Value: {aim_value} | Converted AIM: {converted_aim}")
                language = self.get_or_create_model(Language, 'language', row.get('Language'))
                platform = self.get_or_create_model(Platform, 'platform', row.get('Platform'))
                country = self.get_or_create_model(Country, 'country', row.get('Country'))
                thematic_area = self.get_or_create_model(ThematicArea, 'thematic_area', row.get('Thematic area'))
                
                issn_number = row.get('ISSN Number') if pd.notna(row.get('ISSN Number')) else None
                summary = row.get('Summary') if pd.notna(row.get('Summary')) else None  # Retrieve summary
                # Create a new Journal record
                Journal.objects.create(
                    issn_number=issn_number,  # This can be None
                    journal_title=row.get('Journal tittle ', '').strip(),
                    platform=platform,
                    country=country,
                    publishers_name=row.get('Publishers Name'),
                    language=language,
                    thematic_area=thematic_area,
                    link=row.get('Link'),
                    aim_identifier=converted_aim,
                    medline=self.convert_to_boolean(row.get('Medline (Medicine and Health Journals)')),
                    google_scholar_index=self.convert_to_boolean(row.get('Indexed on Google Scholar')),
                    impact_factor=self.convert_to_int(row.get('Impact Factor')),
                    sjr=self.convert_to_boolean(row.get('Scimago Jornal and Country Rank (SJR); Scopus')),
                    h_index=self.convert_to_int(row.get('H-Index')),
                    eigen_factor=self.convert_to_boolean(row.get('Eigenfactor ')),
                    eigen_metrix=row.get('Eigenfactor metrix'),
                    snip=self.convert_to_boolean(row.get('Source Normalized Impact per Paper (SNIP)')),
                    snip_metrix=self.convert_to_float(row.get('SNIP metrix')),
                    open_access_journal=self.convert_to_boolean(row.get('Open Access Journal')),
                    listed_in_doaj=self.convert_to_boolean(row.get('Journal listed in the Directory of Open Access (DOAJ)')),
                    present_issn=self.convert_to_boolean(row.get('Present on International Standard Serial Number (ISSN) portal')),
                    publisher_in_cope=self.convert_to_boolean(row.get('The publisher is a member of Committee on publication Ethics (COPE)')),
                    online_publisher_africa=self.convert_to_boolean(row.get('Online publisher based in Africa')),
                    hosted_on_inasps=self.convert_to_boolean(row.get("Hosted on INASP'S Journal online")),
                    summary=summary 
                )
                self.stdout.write(f"Inserted row {index}")

            except Exception as e:
                self.stdout.write(self.style.ERROR(f"Error processing row {index}: {e}"))

        self.stdout.write(self.style.SUCCESS('Data loaded successfully.'))

    def get_or_create_model(self, model_class, field_name, value):
        """Helper method to get or create a model instance and return the instance."""
        if pd.notna(value):
            instance, created = model_class.objects.get_or_create(**{field_name: value})
            if created:
                self.stdout.write(self.style.SUCCESS(f"Created new {model_class.__name__} instance with {field_name}: {value}"))
            return instance
        return None

    def convert_to_boolean(self, value):
        """Converts various representations of boolean values to Python's True/False."""
        print(f"Original Value: {value} | Type: {type(value)}")
        if pd.isna(value):
            return None
        if isinstance(value, (int, float)):
            return bool(value)
        value = str(value).strip().lower()
        if value in ['true', '1', 'yes', 'y']:
            return True
        elif value in ['false', '0', 'no', 'n']:
            return False
        return None

    
    def convert_to_int(self, value):
        """Converts a value to an integer, returning None if conversion fails or value is missing."""
        try:
            if pd.isna(value):
                return None
            return int(value)
        except (ValueError, TypeError):
            return None

    
    def convert_to_float(self, value):
        """Converts a value to a float, returning None if conversion fails or value is invalid."""
        try:
            if pd.isna(value):
                return None
            return float(value)
        except (ValueError, TypeError):
            return None
