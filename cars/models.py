from django.db import models


class CarBrand(models.Model):
    name = models.CharField(max_length=100)
    country = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Car(models.Model):
    model_name = models.CharField(max_length=150)
    price = models.DecimalField(max_digits=12, decimal_places=2)
    color = models.CharField(max_length=50)
    year = models.PositiveIntegerField()
    brand = models.ForeignKey(CarBrand, on_delete=models.CASCADE, related_name='cars')

    def __str__(self):
        return f"{self.brand.name} {self.model_name} ({self.year})"
