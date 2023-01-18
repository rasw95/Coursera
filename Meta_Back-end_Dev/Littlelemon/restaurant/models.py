from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.
class booking(models.Model):
    Name = models.CharField(max_length=255, null=False, blank=False)
    No_of_guests = models.IntegerField(default=1, validators=[MaxValueValidator(6),MinValueValidator(1)])
    BookingDate = models.DateTimeField(null=False)
    def __str__(self) -> str:
        return f'{self.Name}' 

class menu(models.Model):
    Title = models.CharField(max_length=255, null=False, blank=False)
    Price =models.DecimalField(max_digits=10, decimal_places=2)
    Inventory = models.SmallIntegerField(default= 0,  validators=[MaxValueValidator(10), MinValueValidator(1)]) 
    def __str__(self) -> str:
        return f'{self.Title} : {self.Price}'


