from django.contrib.auth.models import User
from django.core.management.base import BaseCommand
from django.db import transaction

from glucose.helpers import create_random_levels


class Command(BaseCommand):
    help = "Generate fake data"

    def add_arguments(self, parser):
        parser.add_argument('-u', '--user_id', type=int, help='User id')

    @transaction.atomic
    def handle(self, *args, **options):
        try:
            user = User.objects.filter(id=options.get("user_id")).count()

            if user == 0:
                user = User.objects.create_user("admin", "admin@admin.com", "admin")
            else:
                user = User.objects.get(pk=options.get("user_id"))
            create_random_levels(100, user)
        except Exception as e:
            print(e)
            pass
