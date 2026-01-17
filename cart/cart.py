from decimal import Decimal
from products.models import Product


class Cart:
    def __init__(self, request):
        self.session = request.session
        cart = self.session.get("cart")

        if not cart:
            cart = self.session["cart"] = {}

        self.cart = cart

    def add(self, product, qty=1, override=False):
        product_id = str(product.id)

        if product_id not in self.cart:
            self.cart[product_id] = {
                "qty": 0,
                "price": str(product.price),
                "name": product.name,
                "image": product.image.url if product.image else "",
            }

        if override:
            self.cart[product_id]["qty"] = qty
        else:
            self.cart[product_id]["qty"] += qty

        self.save()


    def remove(self, product):
        product_id = str(product.id)

        if product_id in self.cart:
            del self.cart[product_id]
            self.save()

    def save(self):
        self.session.modified = True

    def __iter__(self):
        for product_id, item in self.cart.items():
            item["id"] = product_id
            item["price"] = Decimal(item["price"])
            item["total"] = item["price"] * item["qty"]
            yield item

    def get_total(self):
        return sum(Decimal(item["price"]) * item["qty"] for item in self.cart.values())

    def clear(self):
        self.session["cart"] = {}
        self.save()
