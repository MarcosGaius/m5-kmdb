from django.core.management.base import BaseCommand, CommandError
from ...models import User
from django.db.utils import IntegrityError


class Command(BaseCommand):
    help = "Create admin users"

    def add_arguments(self, parser) -> None:
        parser.add_argument(
            "-U", "--username", type=str, help="Define the admin's username"
        )
        parser.add_argument(
            "-P", "--password", type=str, help="Define the admin's password"
        )
        parser.add_argument("-E", "--email", type=str, help="Define the admin's email")

    def handle(self, *args, **options):
        username = options["username"] or "admin"
        password = options["password"] or "admin1234"
        email = options["email"] or f"{username}@example.com"

        try:
            user_by_username = User.objects.get(username=username)
            if user_by_username:
                raise CommandError(f"Username `{username}` already taken.")
        except User.DoesNotExist:
            pass

        try:
            user_by_email = User.objects.get(email=email)
            if user_by_email:
                raise CommandError(f"Email `{email}` already taken.")
        except User.DoesNotExist:
            user_data = {
                "username": username,
                "password": password,
                "email": email,
                "is_superuser": True,
            }

            User.objects.create_user(**user_data)

            self.stdout.write(
                self.style.SUCCESS(f"Admin `{username}` successfully created!")
            )
