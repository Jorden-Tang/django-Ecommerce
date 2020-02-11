from django.contrib import admin
from apps.online_shop_index.models import User
from apps.online_shop_dashboard.models import Product, Category


# Register your models here.
admin.site.register(User)
admin.site.register(Product)
admin.site.register(Category)