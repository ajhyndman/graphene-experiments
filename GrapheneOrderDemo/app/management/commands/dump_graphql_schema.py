from django.core.management import BaseCommand
from graphql.utils.schema_printer import print_schema

from ...schema import schema


class Command(BaseCommand):
    def handle(self, **options):
        self.stdout.write(print_schema(schema))
