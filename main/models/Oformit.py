from django.db import models
from main.models.product import Products


class OformitProducts(models.Model):
    name = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=20)
    email = models.EmailField()
    address = models.CharField(max_length=255)
    products = models.ManyToManyField(Products, through='OformitProductItem')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.email}"

class OformitProductItem(models.Model):
    oformit = models.ForeignKey(OformitProducts, on_delete=models.CASCADE)
    product = models.ForeignKey(Products, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.oformit.name} - {self.product.article_number} ({self.quantity} pcs)"