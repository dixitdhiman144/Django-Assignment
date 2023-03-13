from django.core.management.base import BaseCommand
from backup.backup import backup_database

class Command(BaseCommand):
    help = 'Backs up the database and uploads it to AWS S3'

    def handle(self, *args, **options):
        backup_database()
        self.stdout.write(self.style.SUCCESS('Database backup complete'))
