from django.core.management import BaseCommand
from users.models import User
from django.contrib.auth.hashers import make_password

class Command(BaseCommand):
    help = 'Create admin user'

    def handle(self, *args, **options):
        try:
            user, created = User.objects.get_or_create(
                email='admin@admin.com',
                defaults={
                    'password': make_password('1234567'),
                    'is_active': True,
                    'is_staff': True,
                    'is_superuser': True
                }
            )
            if created:
                self.stdout.write(self.style.SUCCESS('Admin user created'))
            else:
                self.stdout.write(self.style.WARNING('Admin user already exists'))
        except Exception as e:
            self.stderr.write(self.style.ERROR(f'Error: {e}'))