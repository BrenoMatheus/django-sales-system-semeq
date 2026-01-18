from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from customers.models import Customer
from products.models import Product
from decimal import Decimal


class Command(BaseCommand):
    help = "Cria dados iniciais para teste do sistema"

    def handle(self, *args, **kwargs):

        # Superusuário
        if not User.objects.filter(username="admin").exists():
            User.objects.create_superuser(
                username="admin",
                email="admin@email.com",
                password="admin123"
            )
            self.stdout.write(self.style.SUCCESS("✔ Admin criado (admin/admin123)"))

        # Cliente comum
        if not User.objects.filter(username="cliente").exists():
            user = User.objects.create_user(
                username="cliente",
                email="cliente@email.com",
                password="123456"
            )

            Customer.objects.create(
                user=user,
                name="Cliente Teste",
                email=user.email
            )

            self.stdout.write(self.style.SUCCESS("✔ Cliente criado (cliente/123456)"))
