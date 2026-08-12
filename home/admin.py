from django.contrib import admin
from .models import contact, Category, Product

# Register your models here.
admin.site.register(contact)
admin.site.register(Category)
admin.site.register(Product)