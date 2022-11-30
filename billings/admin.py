from django.contrib import admin
from .models import Category, Product, Store, Cart
# Register your models here.

admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Store)
admin.site.register(Cart)

