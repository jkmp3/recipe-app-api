"""
Commands to check whether the database is available or not
"""

import time

from django.db import OperationalError
from django.core.management import BaseCommand
from psycopg2.errors import OperationalError as Psycopg2OpError


class Command(BaseCommand):
    """Command to check if the database is available or not"""

    def handle(self, *args, **options):
        """Checks whether the database is available or not"""
        self.stdout.write("Waiting for database...")
        is_db_up = False
        while is_db_up is False:
            try:
                self.check(databases=['default'])
                is_db_up = True
            except(Psycopg2OpError, OperationalError):
                self.stdout.write(
                    "Database unavailable, waiting for 1 second..."
                )
                time.sleep(1)
        self.stdout.write(self.style.SUCCESS('Database available!'))
