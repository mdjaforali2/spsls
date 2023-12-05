from django.contrib import admin
from .models import Category, CustomUser, Position, Employee

admin.site.register(CustomUser)
admin.site.register(Category)
admin.site.register(Position)
admin.site.register(Employee)


# admin.py
import csv
from django.contrib import admin
from django.http import HttpResponse
from .models import Product
from .forms import CSVImportForm  # Import the CSVImportForm

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'price')

    def import_products(self, request, queryset):
        form = CSVImportForm(request.POST, request.FILES)
        if form.is_valid():
            response = HttpResponse(content_type='text/csv')
            response['Content-Disposition'] = 'attachment; filename="import_summary.csv"'
            writer = csv.writer(response)
            writer.writerow(['Product Name', 'Import Status'])

            try:
                csv_file = form.cleaned_data['file']
                decoded_file = csv_file.read().decode('utf-8').splitlines()
                csv_reader = csv.reader(decoded_file)
                next(csv_reader)  # Skip the header row

                for row in csv_reader:
                    name, description, price = row
                    _, created = Product.objects.update_or_create(
                        name=name,
                        defaults={'description': description, 'price': price}
                    )
                    writer.writerow([name, 'Imported' if created else 'Updated'])

            except Exception as e:
                writer.writerow(['Error during import', str(e)])

            return response

    import_products.short_description = "Import Products"

admin.site.register(Product, ProductAdmin)


