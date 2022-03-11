from django.db import models

# Create your models here.

class traveldb(models.Model):
    destination=models.CharField(max_length=200,null=True,blank=False)
    location=models.CharField(max_length=200,null=True,blank=False)
    photo = models.ImageField(upload_to='image',default=0)
    price=models.IntegerField(null=True,blank=False)


