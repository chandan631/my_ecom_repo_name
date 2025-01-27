from django.db import models
from my_shop.models import Product
from django.contrib.auth.models import User

# Cart Model
class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.user.username}'s cart - {self.product.name} (x{self.quantity})"


# Order Model
class Order(models.Model):
    STATUS_CHOICES = (
        ('Placed', 'Placed'),
        ('Shipped', 'Shipped'),
        ('Delivered', 'Delivered'),
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Placed')

    def __str__(self):
        return f"Order {self.id} - {self.user.username} - {self.status}"
