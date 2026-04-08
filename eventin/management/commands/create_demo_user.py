from django.core.management.base import BaseCommand
from django.contrib.auth.models import User


class Command(BaseCommand):
    help = 'Create demo user if not exists'

    def handle(self, *args, **kwargs):
        username = 'demo_user'
        password = 'Demo1234!'

        if not User.objects.filter(username=username).exists():
            User.objects.create_user(
                username=username,
                password=password,
                email='demo@example.com'
            )
            self.stdout.write(self.style.SUCCESS('Demo user created'))
        else:
            self.stdout.write(self.style.WARNING('Demo user already exists'))
