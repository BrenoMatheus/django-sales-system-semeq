from django.core.management.base import BaseCommand
from django.core.management import call_command


class Command(BaseCommand):
    help = "Executa todas as seeds do projeto"

    def handle(self, *args, **kwargs):

        self.stdout.write("🌱 Rodando seeds de usuários...")
        call_command("seed_accounts")

        self.stdout.write("🌱 Rodando seeds de customers...")
        call_command("seed_customers")

        self.stdout.write("🌱 Rodando seeds de produtos...")
        call_command("seed_products")

        self.stdout.write(self.style.SUCCESS("✅ Todas as seeds executadas com sucesso!"))
