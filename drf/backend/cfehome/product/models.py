from tkinter import CASCADE
from django.db import models
from django.contrib.auth.models import User




class Product(models.Model):
    title=models.CharField(max_length=64);
    price=models.DecimalField(max_digits=5,decimal_places=3);
    content=models.CharField(max_length=2048);

    @property
    def double_price(self):
        return self.price*2;

    def get_discount(self):
        return 11;    



class Product_comments(models.Model):
    product=models.ForeignKey(Product,on_delete=models.CASCADE);
    comment=models.CharField(max_length=2048);



class Carpets(models.Model):
    name=models.CharField(max_length=255);
    year=models.PositiveIntegerField();
    

 







    



# Create your models here.
