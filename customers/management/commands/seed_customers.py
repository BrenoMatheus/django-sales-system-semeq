from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from customers.models import Customer

class Command(BaseCommand):
    help = "Cria clientes de teste"

    def handle(self, *args, **kwargs):
        self.stdout.write(self.style.WARNING("Seed de customers iniciado..."))

        for i in range(1, 5):
            username = f"cliente{i}"
            email = f"cliente{i}@email.com"

            user, created = User.objects.get_or_create(
                username=username,
                defaults={"email": email, "password": "123456"}
            )

            Customer.objects.get_or_create(
                user=user,
                defaults={"name": f"Cliente {i}", "email": email}
            )

        self.stdout.write(self.style.SUCCESS("Clientes criados com sucesso."))
        self.stdout.write(self.style.SUCCESS("Seed de customers finalizado."))
