from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

class CarMake(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    country = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return self.name

class CarModel(models.Model):
    CAR_TYPES = [
        ('SEDAN', 'Sedan'),
        ('SUV', 'SUV'),
        ('WAGON', 'Wagon'),
    ]

    car_make = models.ForeignKey('CarMake', on_delete=models.CASCADE)  # Use string here
    dealer_id = models.IntegerField(null=True, blank=True)   
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=10, choices=CAR_TYPES, default='SUV')
    year = models.IntegerField(
        validators=[MinValueValidator(2015), MaxValueValidator(2023)],
        default=2023
    )
    color = models.CharField(max_length=30, blank=True, null=True)

    def __str__(self):
        return f"{self.car_make.name} {self.name}"