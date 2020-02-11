from django.db import models
from apps.online_shop_dashboard.models import Product
from datetime import datetime

class Personal_Manager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        if len(postData['first_name']) < 2:
            errors['first_name'] = "First Name is too short"
        if len(postData['last_name']) < 2:
            errors['last_name'] = "Last Name is too short"
        if(postData['password'] != postData['confirm_password']):
            errors['password'] = "Password != confirm Password"
        return errors

class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    is_admin = models.BooleanField(default = False)
    phone_number = models.CharField( max_length =10, null = True)
    address = models.CharField(max_length=255, null = True)
    address_2 = models.CharField(max_length=255, null = True)
    city = models.CharField(max_length=50, null = True)
    zip_code = models.CharField(max_length=5, null = True)
    shopping_cart = models.ManyToManyField(Product, related_name = "buying_users")
    buy_it_later = models.ManyToManyField(Product, related_name = "interested_users")
    updated_at = models.DateTimeField(auto_now=True)
    added_at =  models.DateTimeField(auto_now_add=True)
    objects = Personal_Manager()












