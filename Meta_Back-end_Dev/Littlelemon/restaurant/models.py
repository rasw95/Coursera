from django.db import models


# Create your models here.
class Booking(models.Model):
    first_name = models.CharField(max_length=200, default="NA")
    reservation_date = models.DateField(default=None)
    reservation_slot = models.SmallIntegerField(default=10)
    def __str__(self): 
        return self.first_name



class Category(models.Model):
    slug = models.SlugField()
    title = models.CharField(max_length=255, db_index= True) #DB index fast searching. 
    def __str__(self) -> str:
        return self.title

class MenuItem(models.Model):
    name = models.CharField(max_length=200, default='NA')
    price = models.IntegerField()
    description = models.TextField(max_length=1000, default='No Description')
    category = models.ForeignKey(Category, on_delete= models.PROTECT)
    def __str__(self):
      return self.name
  