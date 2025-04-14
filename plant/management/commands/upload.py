from django.core.management.base import BaseCommand
from plant.converter import migrate_csv_file

class Command(BaseCommand):
    help = 'Upload and process CSV file containing plant data'

    def add_arguments(self, parser):
        parser.add_argument('filename', type=str, help='CSV file to process')

    def handle(self, *args, **options):
        filename = options['filename']
        try:
            self.stdout.write(self.style.HTTP_INFO(f'Processing file: {filename}'))
            result = migrate_csv_file(filename)
            self.stdout.write(self.style.SUCCESS(result))
        except Exception as e:
            self.stdout.write(self.style.ERROR(f'Error processing file: {str(e)}'))