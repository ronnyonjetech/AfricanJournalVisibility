# import pandas as pd
# from django.core.management.base import BaseCommand
# from journalApis.models import Language, Platform, Country, ThematicArea, Journal

# class Command(BaseCommand):
#     help = 'Load data from an Excel file into the database.'

#     def add_arguments(self, parser):
#         parser.add_argument('excel_file_path', type=str, help='Path to the Excel file to be loaded.')

#     def handle(self, *args, **kwargs):
#         excel_file_path = kwargs['excel_file_path']

#         # Load the Excel spreadsheet
#         df = pd.read_excel(excel_file_path)

#         # Iterate over the rows in the DataFrame
#         for index, row in df.iterrows():
#             language = Language.objects.get_or_create(language=row['Language'])[0] if pd.notna(row['Language']) else None
#             platform = Platform.objects.get_or_create(platform=row['Platform'])[0] if pd.notna(row['Platform']) else None
#             country = Country.objects.get_or_create(country=row['Country'])[0] if pd.notna(row['Country']) else None
#             thematic_area = ThematicArea.objects.get_or_create(thematic_area=row['Thematic area'])[0] if pd.notna(row['Thematic area']) else None

#             issn_number = row['ISSN Number'] if pd.notna(row['ISSN Number']) else None

#             # Use ISSN Number as the identifier if it's provided; otherwise, create a new record with a null ISSN
#             Journal.objects.update_or_create(
#                 issn_number=issn_number,  # This can now be None (null in the database)
#                 defaults={
#                     'journal_title': row['Journal tittle '].strip(),
#                     'platform': platform,
#                     'country': country,
#                     'publishers_name': row['Publishers Name'] if pd.notna(row['Publishers Name']) else None,
#                     'language': language,
#                     'thematic_area': thematic_area,
#                     'link': row['Link'] if pd.notna(row['Link']) else None,
#                     'aim_identifier': bool(row['African Index Medicus']) if pd.notna(row['African Index Medicus']) else False,
#                     'medline': bool(row['Medline (Medicine and Health Journals)']) if pd.notna(row['Medline (Medicine and Health Journals)']) else False,
#                     'google_scholar_index': bool(row['Indexed on Google Scholar']) if pd.notna(row['Indexed on Google Scholar']) else False,
#                     'impact_factor': int(row['Impact Factor']) if pd.notna(row['Impact Factor']) else None,
#                     'sjr': bool(row['Scimago Jornal and Country Rank (SJR); Scopus']) if pd.notna(row['Scimago Jornal and Country Rank (SJR); Scopus']) else False,
#                     'h_index': int(row['H-Index']) if pd.notna(row['H-Index']) else None,
#                     'eigen_factor': bool(row['Eigenfactor ']) if pd.notna(row['Eigenfactor ']) else False,
#                     'eigen_metrix': row['Eigenfactor metrix'] if pd.notna(row['Eigenfactor metrix']) else None,
#                     'snip': bool(row['Source Normalized Impact per Paper (SNIP)']) if pd.notna(row['Source Normalized Impact per Paper (SNIP)']) else False,
#                     'snip_metrix': float(row['SNIP metrix']) if pd.notna(row['SNIP metrix']) else None,
#                     'open_access_journal': bool(row['Open Access Journal']) if pd.notna(row['Open Access Journal']) else False,
#                     'listed_in_doaj': bool(row['Journal listed in the Directory of Open Access (DOAJ)']) if pd.notna(row['Journal listed in the Directory of Open Access (DOAJ)']) else False,
#                     'present_issn': bool(row['Present on International Standard Serial Number (ISSN) portal']) if pd.notna(row['Present on International Standard Serial Number (ISSN) portal']) else False,
#                     'publisher_in_cope': bool(row['The publisher is a member of Committee on publication Ethics (COPE)']) if pd.notna(row['The publisher is a member of Committee on publication Ethics (COPE)']) else False,
#                     'online_publisher_africa': bool(row['Online publisher based in Africa']) if pd.notna(row['Online publisher based in Africa']) else False,
#                     'hosted_on_inasps': bool(row["Hosted on INASP'S Journal online"]) if pd.notna(row["Hosted on INASP'S Journal online"]) else False,
#                 }
#             )

#         self.stdout.write(self.style.SUCCESS('Data loaded successfully.'))

# #test101
# #python manage.py load_excel_data "C:\Users\guest478\Downloads\visibility.xlsx"


# import pandas as pd
# from django.core.management.base import BaseCommand
# from journalApis.models import Language, Platform, Country, ThematicArea, Journal

# class Command(BaseCommand):
#     help = 'Load data from an Excel file into the database.'

#     def add_arguments(self, parser):
#         parser.add_argument('excel_file_path', type=str, help='Path to the Excel file to be loaded.')

#     def handle(self, *args, **kwargs):
#         excel_file_path = kwargs['excel_file_path']

#         # Load the Excel spreadsheet
#         df = pd.read_excel(excel_file_path)
#         self.stdout.write(self.style.SUCCESS(f"Loaded {df.shape[0]} rows from the Excel file."))

#         # Iterate over the rows in the DataFrame
#         for index, row in df.iterrows():
#             try:
#                 language = self.get_or_create_model(Language, 'language', row.get('Language'))
#                 platform = self.get_or_create_model(Platform, 'platform', row.get('Platform'))
#                 country = self.get_or_create_model(Country, 'country', row.get('Country'))
#                 thematic_area = self.get_or_create_model(ThematicArea, 'thematic_area', row.get('Thematic area'))
                
#                 issn_number = row.get('ISSN Number') if pd.notna(row.get('ISSN Number')) else None

#                 # Create a new Journal record
#                 Journal.objects.create(
#                     issn_number=issn_number,  # This can be None
#                     journal_title=row.get('Journal tittle ', '').strip(),
#                     platform=platform,
#                     country=country,
#                     publishers_name=row.get('Publishers Name'),
#                     language=language,
#                     thematic_area=thematic_area,
#                     link=row.get('Link'),
#                     aim_identifier=self.convert_to_boolean(row.get('African Index Medicus')),
#                     medline=self.convert_to_boolean(row.get('Medline (Medicine and Health Journals)')),
#                     google_scholar_index=self.convert_to_boolean(row.get('Indexed on Google Scholar')),
#                     impact_factor=self.convert_to_int(row.get('Impact Factor')),
#                     sjr=self.convert_to_boolean(row.get('Scimago Jornal and Country Rank (SJR); Scopus')),
#                     h_index=self.convert_to_int(row.get('H-Index')),
#                     eigen_factor=self.convert_to_boolean(row.get('Eigenfactor ')),
#                     eigen_metrix=row.get('Eigenfactor metrix'),
#                     snip=self.convert_to_boolean(row.get('Source Normalized Impact per Paper (SNIP)')),
#                     snip_metrix=self.convert_to_float(row.get('SNIP metrix')),
#                     open_access_journal=self.convert_to_boolean(row.get('Open Access Journal')),
#                     listed_in_doaj=self.convert_to_boolean(row.get('Journal listed in the Directory of Open Access (DOAJ)')),
#                     present_issn=self.convert_to_boolean(row.get('Present on International Standard Serial Number (ISSN) portal')),
#                     publisher_in_cope=self.convert_to_boolean(row.get('The publisher is a member of Committee on publication Ethics (COPE)')),
#                     online_publisher_africa=self.convert_to_boolean(row.get('Online publisher based in Africa')),
#                     hosted_on_inasps=self.convert_to_boolean(row.get("Hosted on INASP'S Journal online")),
#                 )
#                 self.stdout.write(f"Inserted row {index}")

#             except Exception as e:
#                 self.stdout.write(self.style.ERROR(f"Error processing row {index}: {e}"))

#         self.stdout.write(self.style.SUCCESS('Data loaded successfully.'))

#     def get_or_create_model(self, model_class, field_name, value):
#         """Helper method to get or create a model instance and return the instance."""
#         if pd.notna(value):
#             instance, created = model_class.objects.get_or_create(**{field_name: value})
#             if created:
#                 self.stdout.write(self.style.SUCCESS(f"Created new {model_class.__name__} instance with {field_name}: {value}"))
#             return instance
#         return None

#     def convert_to_boolean(self, value):
#         """Converts various representations of boolean values to Python's True/False."""
#         if pd.isna(value):
#             return None
#         value = str(value).strip().lower()
#         if value in ['true', '1', 'yes', 'y']:
#             return True
#         elif value in ['false', '0', 'no', 'n']:
#             return False
#         return None

#     def convert_to_int(self, value):
#         """Converts a value to an integer, returning None if conversion fails or value is missing."""
#         try:
#             return int(value)
#         except (ValueError, TypeError):
#             return None

#     def convert_to_float(self, value):
#         """Converts a value to a float, returning None if conversion fails or value is missing."""
#         try:
#             return float(value)
#         except (ValueError, TypeError):
#             return None

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
                language = self.get_or_create_model(Language, 'language', row.get('Language'))
                platform = self.get_or_create_model(Platform, 'platform', row.get('Platform'))
                country = self.get_or_create_model(Country, 'country', row.get('Country'))
                thematic_area = self.get_or_create_model(ThematicArea, 'thematic_area', row.get('Thematic area'))
                
                issn_number = row.get('ISSN Number') if pd.notna(row.get('ISSN Number')) else None

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
                    aim_identifier=self.convert_to_boolean(row.get('African Index Medicus')),
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
        if pd.isna(value):
            return None
        value = str(value).strip().lower()
        if value in ['true', '1', 'yes', 'y']:
            return True
        elif value in ['false', '0', 'no', 'n']:
            return False
        return None

    def convert_to_int(self, value):
        """Converts a value to an integer, returning None if conversion fails or value is missing."""
        try:
            return int(value)
        except (ValueError, TypeError):
            return None

    def convert_to_float(self, value):
        """Converts a value to a float, returning None if conversion fails or value is missing."""
        try:
            return float(value)
        except (ValueError, TypeError):
            return None
