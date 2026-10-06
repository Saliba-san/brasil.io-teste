"""Prepara usuário sintético para avaliação no ambiente efêmero."""
import os

from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand, CommandError


class Command(BaseCommand):
    help = "Prepara usuário comum de teste no ambiente de integração."

    def handle(self, *args, **options):
        if os.environ.get("INTEGRATION_BOOTSTRAP") != "true":
            raise CommandError("Comando permitido apenas no Compose de integração.")
        username = os.environ.get("INTEGRATION_TEST_USERNAME")
        password = os.environ.get("INTEGRATION_TEST_PASSWORD")
        if not username or not password:
            raise CommandError("Configure usuário e senha sintéticos de integração.")
        user, _ = get_user_model().objects.get_or_create(username=username)
        if user.is_staff or user.is_superuser:
            raise CommandError("O usuário de teste não pode ter privilégios administrativos.")
        user.email = "zap@example.invalid"
        user.is_active = True
        user.set_password(password)
        user.save()
        self.stdout.write("Usuário comum de integração preparado.")
