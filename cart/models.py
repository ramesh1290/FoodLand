from django.db import models
from django.contrib.auth.models import User
from products.models import Product

# Cart Model
class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)  # To handle active/inactive carts

    def total_price(self):
        # Sum of all cart items' total prices
        return sum(item.total_price() for item in self.cartitems.all())

    def total_items(self):
        # Count all cart items
        return self.cartitems.count()

    def __str__(self):
        return f"Cart {self.id} - {self.user.username if self.user else 'Guest'}"


# CartItem Model
class CartItem(models.Model):
    cart = models.ForeignKey(Cart, related_name="cartitems", on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def total_price(self):
        # Calculate total price of the item (price * quantity)
        return self.quantity * self.product.price

    def __str__(self):
        return f"{self.quantity} x {self.product.name}"
