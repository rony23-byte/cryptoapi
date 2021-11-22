from django.db import models

# Create your models here.
class Cryptocurrency(models.Model):
    cryptocurrency= models.CharField(max_length=20)
    price=models.DecimalField(max_digits=10,decmial_places=8)
    market_cap=models.IntergerField(max_length=100)
    change=models.models.DecimalField( max_digits=5, decimal_places=2)

    #print an instance of the crypricurrency 
    def __str__(self) -> str:
        return  self.cryptocurrency
