from django.core.management.base import BaseCommand
from customers.models import Customer


class Command(BaseCommand):
    help = "Cria clientes de teste"

    def handle(self, *args, **kwargs):
        self.stdout.write(self.style.WARNING("Seed de customers iniciado..."))

        for i in range(1, 11):
            Customer.objects.get_or_create(
                email=f"cliente{i}@email.com",
                defaults={
                    "name": f"Cliente {i}"
                }
            )

        self.stdout.write(self.style.SUCCESS("Clientes criados com sucesso."))
        self.stdout.write(self.style.SUCCESS("Seed de customers finalizado."))
