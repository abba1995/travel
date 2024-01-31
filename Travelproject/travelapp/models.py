from django.db import models
from django.db.models import ImageField


# Create your models here.
class Place(models.Model):
    name= models.CharField(max_length=250)
    img=ImageField(upload_to='pics')
    desc = models.TextField()

    def __str__(self):
     return self.name

class Meet(models.Model):
    n= models.CharField(max_length=250)
    im= ImageField(upload_to='pics')
    d= models.TextField()

    def __str__(self):
     return self.n