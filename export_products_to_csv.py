import os
import csv
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'bismillah_bazar.settings')
application = get_wsgi_application()

from store.models import Product  # Replace 'your_app_name' with your actual app name

def export_products_to_csv(file_path):
    # Fetch only the necessary fields from the database
    products = Product.objects.values('name', 'description', 'price')

    # Define the CSV file headers
    headers = ['name', 'description', 'price']

    # Open the CSV file for writing
    with open(file_path, 'w', newline='') as csv_file:
        writer = csv.writer(csv_file)
        
        # Write the headers to the CSV file
        writer.writerow(headers)

        # Write each product's data to the CSV file
        for product in products:
            writer.writerow([
                product['name'],
                product['description'],
                product['price'],
            ])

if __name__ == "__main__":
    # Specify the file path for the CSV file
    csv_file_path = 'files/products_export.csv'

    # Call the export function
    export_products_to_csv(csv_file_path)

    print(f"Products exported to {csv_file_path}")
