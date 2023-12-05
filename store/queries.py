# your_app/queries.py

from .models import Product

def update_quantity_in_stock():
    # Update all existing products to have a quantity in stock of 100
    Product.objects.all().update(quantity_in_stock=100)
