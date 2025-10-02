from django.db import models

# Create your models here.
class Car(models.Model):
    PURPOSE_CHOICES = [
        ('daily', 'Daily Commute'),
        ('family', 'Family Use'),
        ('luxury', 'Luxury'),
        ('sport', 'Sport/Performance'),
        ('offroad', 'Off-Road/Adventure'),
    ]

    TYPE_CHOICES = [
        ('sedan', 'Sedan'),
        ('suv', 'SUV'),
        ('hatchback', 'Hatchback'),
        ('truck', 'Truck'),
        ('coupe', 'Coupe'),
        ('coupe', 'Coupe'),
        ('conertible', 'Convertible')
    ]

    name = models.CharField(max_length = 200)
    brand = models.CharField(max_length = 100)
    price = models.DecimalField(max_digits = 10, decimal_places=2)
    purpose = models.CharField(max_length = 20, choices=PURPOSE_CHOICES)
    car_type = models.CharField(max_length = 20, choices=TYPE_CHOICES)
    description = models.TextField()
    features = models.TextField(help_text="Comma-separated features")
    image_Url = models.URLField(max_length=500, help_text="External image URL")

    class Meta:
        ordering = ['price']

    def __str__(self):
        return f"{self.brand} {self.name}"