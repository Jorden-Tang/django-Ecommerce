from django.db import models

class Product_Manager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        if len(postData['name']) < 3:
            errors['product_name'] = "product name is too short"
        if len(postData['details']) <= 0:
            errors['details'] = "please add description of your product"
        return errors
        

class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    details = models.TextField()
    image = models.FileField(upload_to="online_shop_dashboard/images", max_length=100, null = True)
    updated_at = models.DateTimeField(auto_now=True)
    added_at =  models.DateTimeField(auto_now_add=True)
    objects = Product_Manager()

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=50)
    products = models.ManyToManyField(Product, related_name = "categories")
    updated_at = models.DateTimeField(auto_now=True)
    added_at =  models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

