from django.db import models

class Product(models.Model):
    product = models.CharField(max_length=100)
    code = models.CharField(max_length=4)
    description = models.TextField(blank=True)
    price = models.FloatField()

    def __str__(self) -> str:
        return f"{self.product} - {self.code} - {self.price}"
# Create your models here.
