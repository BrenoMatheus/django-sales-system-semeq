from django.test import TestCase
from decimal import Decimal
from django.contrib.auth.models import User
from customers.models import Customer
from products.models import Product
from sales.models import Sale, SaleItem
from django.utils import timezone
from django.urls import reverse

class SaleItemModelTest(TestCase):

    def test_subtotal_calculation(self):
        # cria usuário e customer
        user = User.objects.create_user(username="teste", password="123")
        customer = Customer.objects.create(user=user, name="Cliente Teste", email="teste@email.com")

        # cria produto
        product = Product.objects.create(
            name="Produto Teste",
            price=Decimal("10.00")
        )

        # cria venda
        sale = Sale.objects.create(
            customer=customer,
            sale_date=timezone.now().date(),
            cep="12345678",
            street="Rua Teste",
            neighborhood="Centro",
            city="SP",
            state="SP"
        )

        # cria item
        item = SaleItem.objects.create(
            sale=sale,
            product=product,
            quantity=3,
            unit_price=Decimal("10.00")
        )

        # verifica subtotal
        self.assertEqual(item.subtotal(), Decimal("30.00"))

class SalesHistoryViewTest(TestCase):

    def test_history_requires_login(self):
        response = self.client.get("/vendas/historico/")

        # Django redireciona para login (302)
        self.assertEqual(response.status_code, 302)
        self.assertTrue("/accounts/login/" in response.url)

