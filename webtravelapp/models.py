from django.db import models

# Create your models here.

class contactdb(models.Model):
    Name=models.CharField(max_length=200,null=True,blank=False)
    Email=models.EmailField(max_length=200,null=True,blank=False)
    Phone=models.IntegerField(null=True,blank=False)
    Subject=models.CharField(max_length=200,null=True,blank=False)
    Message=models.CharField(max_length=200,null=True,blank=False)
class registerdb(models.Model):
    firstname=models.CharField(max_length=200,null=True,blank=False)
    lastname=models.EmailField(max_length=200,null=True,blank=False)
    phonenumber=models.IntegerField(null=True,blank=False)
    username=models.CharField(max_length=200,null=True,blank=False)
    password=models.CharField(max_length=200,null=True,blank=False)



