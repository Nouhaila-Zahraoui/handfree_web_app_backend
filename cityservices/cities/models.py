from django.db import models

# cities/models.py
from django.db import models

class City(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    date = models.DateField()
    description = models.TextField()

    def __str__(self):
        return self.name
