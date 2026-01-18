from django.conf import settings
from django.db import models

class Customer(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="customer",
        null=True,
        blank=True
    )

    name = models.CharField(max_length=150)
    email = models.EmailField()
    # outros campos...
