from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from relationship_app.models import UserProfile

class Command(BaseCommand):
    help = 'Create a user with a specific role'

    def add_arguments(self, parser):
        parser.add_argument('username', type=str, help='Username of the new user')
        parser.add_argument('password', type=str, help='Password of the new user')
        parser.add_argument('role', type=str, help='Role of the new user (Admin, Librarian, Member)')

    def handle(self, *args, **kwargs):
        username = kwargs['username']
        password = kwargs['password']
        role = kwargs['role']

        # Create the user or get the existing one
        user, created = User.objects.get_or_create(username=username)
        if created:
            user.set_password(password)
            user.save()

        # Check if the user already has a UserProfile
        if not UserProfile.objects.filter(user=user).exists():
            UserProfile.objects.create(user=user, role=role)
            self.stdout.write(self.style.SUCCESS(f'Successfully created user {username} with role {role}'))
        else:
            self.stdout.write(self.style.WARNING(f'User {username} already has a profile.'))
