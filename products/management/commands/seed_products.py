from django.core.management.base import BaseCommand
from products.models import Category, Supplier, Product
from decimal import Decimal
import random


class Command(BaseCommand):
    help = "Cria dados iniciais de categorias, fornecedores e produtos"

    def handle(self, *args, **kwargs):
        self.stdout.write(self.style.WARNING("Seed de products iniciado..."))

        # Categorias
        categories_names = [
            "Eletrônicos", "Livros", "Roupas", "Casa", "Esporte"
        ]

        categories = []
        for name in categories_names:
            category, _ = Category.objects.get_or_create(name=name)
            categories.append(category)

        self.stdout.write(self.style.SUCCESS(f"{len(categories)} categorias criadas."))

        # Fornecedores
        suppliers_data = [
            {"name": "Fornecedor Alpha", "email": "alpha@email.com"},
            {"name": "Fornecedor Beta", "email": "beta@email.com"},
            {"name": "Fornecedor Gama", "email": "gama@email.com"},
        ]

        suppliers = []
        for data in suppliers_data:
            supplier, _ = Supplier.objects.get_or_create(**data)
            suppliers.append(supplier)

        self.stdout.write(self.style.SUCCESS(f"{len(suppliers)} fornecedores criados."))

        # Produtos
        for i in range(1, 16):
            product, created = Product.objects.get_or_create(
                name=f"Produto {i}",
                defaults={
                    "description": "Produto de teste",
                    "price": Decimal(random.randint(10, 300)),
                    "stock": random.randint(1, 100),
                    "category": random.choice(categories),
                }
            )

            if created:
                product.suppliers.set(
                    random.sample(suppliers, k=random.randint(1, len(suppliers)))
                )

        self.stdout.write(self.style.SUCCESS("Produtos criados com sucesso."))
        self.stdout.write(self.style.SUCCESS("Seed de products finalizado."))
