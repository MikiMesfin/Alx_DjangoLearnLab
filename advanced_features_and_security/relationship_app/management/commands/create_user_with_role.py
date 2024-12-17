from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from relationship_app.models import UserProfile

class Command(BaseCommand):
    help = 'Create a user with a specific role'

    def add_arguments(self, parser):
        parser.add_argument('username', type=str)
        parser.add_argument('password', type=str)
        parser.add_argument('role', type=str)

    def handle(self, *args, **kwargs):
        username = kwargs['username']
        password = kwargs['password']
        role = kwargs['role']

        # Check if the user already exists
        user, created = User.objects.get_or_create(username=username)
        if created:
            user.set_password(password)
            user.save()
            self.stdout.write(self.style.SUCCESS(f'User "{username}" created successfully.'))
        else:
            self.stdout.write(self.style.WARNING(f'User "{username}" already exists.'))

        # Check if UserProfile already exists for the user
        user_profile, profile_created = UserProfile.objects.get_or_create(user=user)
        if profile_created:
            user_profile.role = role
            user_profile.save()
            self.stdout.write(self.style.SUCCESS(f'UserProfile created with role "{role}" for user "{username}".'))
        else:
            user_profile.role = role  # Update role if needed
            user_profile.save()
            self.stdout.write(self.style.WARNING(f'UserProfile updated with role "{role}" for user "{username}".'))
