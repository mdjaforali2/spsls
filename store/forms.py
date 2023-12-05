# forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from store.models import CustomUser, Employee

class CustomUserCreationForm(UserCreationForm):
    
    # Adding province and city fields
    division = forms.ChoiceField(choices=CustomUser.DIVISION_CHOICES, required=True)
    city = forms.CharField(max_length=255, required=True)

    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'password1', 'password2', 'phone_number', 'division', 'city']

    def __init__(self, *args, **kwargs):
        super(CustomUserCreationForm, self).__init__(*args, **kwargs)

        # Set the default value for the division field
        self.fields['division'].initial = CustomUser.CHITTAGONG

    # Override clean_division to set the default value if not provided
    def clean_division(self):
        division = self.cleaned_data['division']
        return division or CustomUser.CHITTAGONG



class CustomAuthenticationForm(AuthenticationForm):
    class Meta:
        model = CustomUser



# forms.py
from django import forms
from .models import Product
import csv

# forms.py
from django import forms
from .models import Product

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['category', 'name', 'description', 'price', 'image']

    # Make category and quantity_in_stock optional
    def __init__(self, *args, **kwargs):
        super(ProductForm, self).__init__(*args, **kwargs)
        self.fields['category'].required = False



# forms.py
import csv
from django import forms
from .models import Product

class CSVImportForm(forms.Form):
    file = forms.FileField(label='CSV File')

    def clean_file(self):
        file = self.cleaned_data['file']
        if file:
            # Check if the file has a .csv extension
            if not file.name.endswith('.csv'):
                raise forms.ValidationError('File must be a CSV file.')

            # Add additional validation or processing logic here if needed
            
        return file

    def handle_uploaded_file(self, file):
        decoded_file = file.read().decode('utf-8').splitlines()

        # Skip the header row
        csv_reader = csv.reader(decoded_file)
        next(csv_reader)

        num_products = 0
        for row in csv_reader:
            name, description, price = row
            # Create or update the Product instance
            _, created = Product.objects.update_or_create(
                name=name,
                defaults={'description': description, 'price': price}
            )
            num_products += 1

        return num_products





from .models import Product
from django import forms

class ProductAttributesForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['size', 'color']