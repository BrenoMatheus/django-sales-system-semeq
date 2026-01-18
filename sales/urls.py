from django.urls import path
from . import views

urlpatterns = [
    path('nova/', views.create_sale, name='create_sale'),
    path("checkout/", views.checkout, name="checkout"),
    path("sucesso/", views.order_success, name="order_success")

]
