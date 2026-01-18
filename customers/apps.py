# customers/apps.py
from django.apps import AppConfig

class CustomersConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'customers'

    def ready(self):
        from django.contrib.auth.models import User
        from customers.models import Customer

        if not User.objects.filter(username="dev").exists():
            user = User.objects.create_user(
                username="dev",
                password="123456",
                email="dev@email.com"
            )

            Customer.objects.create(
                user=user,
                name="Usuário Dev",
                email="dev@email.com"
            )
