from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from .models import Product
from .cart import Cart
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from .forms import CustomUserCreationForm, CustomAuthenticationForm
from django.contrib import messages
from django.views.generic import TemplateView

def main_page(request):
    return render(request, 'store/main.html')

def product_list(request):
    products = Product.objects.all()
    return render(request, 'store/product_list.html', {'products': products, 'title': 'Product List'})

def product_detail(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    return render(request, 'store/product_detail.html', {'product': product})

def process_order(request):
    # Implement order processing logic here
    # Capture customer information, handle payment, update inventory, etc.
    # After processing, you may want to clear the cart and show an order confirmation page
    return render(request, 'store/order_confirmation.html')




def customer_signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user, backend='django.contrib.auth.backends.ModelBackend')
            messages.success(request, f"Account created successfully. Welcome, {user.username}!")
            return redirect('main_page')
        else:
            # Handle form validation errors
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f"Error in {field}: {error}")

    else:
        form = CustomUserCreationForm()

    return render(request, 'registration/signup.html', {'form': form})






def login_view(request):
    if request.method == 'POST':
        form = CustomAuthenticationForm(request, request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(request, f"Welcome back, {user.username}!")
            return redirect('main_page')
        else:
            # Handle form validation errors
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f"Error in {field}: {error}")
    else:
        form = CustomAuthenticationForm()
    return render(request, 'registration/login.html', {'form': form})



def user_logout(request):
    logout(request)
    messages.success(request, "You have been successfully logged out. Come back soon!")
    return redirect('logout_success')

class LogoutSuccessView(TemplateView):
    template_name = 'registration/logout.html'




# views.py

# views.py
from django.shortcuts import render, redirect
from .forms import ProductForm

def add_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            # Handle the form data to add a single product
            # For example, you might save the form data to the database
            form.save()
            # Add a success message
            messages.success(request, 'Product added successfully.')
            return redirect('product_list')  # Redirect to the product list page
        else:
            # Print form errors for debugging
            print(form.errors)
            # Add an error message
            messages.error(request, 'Error adding the product. Please check the form.')
    else:
        form = ProductForm()

    return render(request, 'store/add_product.html', {'form': form})


# views.py
from django.contrib import messages
from django.shortcuts import render, redirect
from .forms import CSVImportForm
from .models import Product

def add_file(request):
    if request.method == 'POST':
        form = CSVImportForm(request.POST, request.FILES)
        if form.is_valid():
            file = form.cleaned_data['file']
            # Handle the CSV file upload logic
            num_products = form.handle_uploaded_file(file)

            # Add a success message
            messages.success(request, f'Successfully imported {num_products} products from the CSV file.')

            return redirect('product_list')  # Redirect to the product list page
    else:
        form = CSVImportForm()

    return render(request, 'store/add_file.html', {'form': form})




# views.py
from django.contrib.auth.decorators import user_passes_test

@user_passes_test(lambda u: u.is_staff, login_url='login')
def manage_product(request, product_id):
    product = get_object_or_404(Product, pk=product_id)

    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, 'Product details updated successfully.')
            return redirect('product_detail', product_id=product.id)
        else:
            messages.error(request, 'Error updating product details. Please check the form.')
    else:
        form = ProductForm(instance=product)

    return render(request, 'store/manage_product.html', {'form': form, 'product': product})



from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from .models import Product
from .cart import Cart
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from .forms import CustomUserCreationForm, CustomAuthenticationForm
from django.contrib import messages
from django.views.generic import TemplateView

# ... (Your existing imports)

def view_cart(request):
    cart = Cart(request)
    return render(request, 'store/shopping_cart.html', {'cart': cart})

def add_to_cart(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    cart = Cart(request)

    # Get the requested quantity (default to 1 if not provided)
    quantity = int(request.POST.get('quantity', 1))

    # # Check if the requested quantity is available
    # if quantity > product.quantity_in_stock:
    #     messages.error(request, f"Sorry, only {product.quantity_in_stock} units are available.")
    #     return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

    cart.add(product, quantity)
    messages.success(request, f"{product.name} added to the cart.")
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

def update_cart(request):
    if request.method == 'POST':
        product_id = request.POST.get('product_id')
        quantity = int(request.POST.get('quantity', 1))  # Default to 1 if quantity is not provided

        if product_id:
            product = get_object_or_404(Product, pk=product_id)
            cart = Cart(request)
            cart.update(product, quantity)

    return redirect('view_cart')

def remove_from_cart(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    cart = Cart(request)
    cart.remove(product)
    messages.success(request, f"{product.name} removed from the cart.")
    return redirect('view_cart')

def clear_cart(request):
    cart = Cart(request)
    cart.clear()
    messages.success(request, "Cart cleared.")
    return redirect('view_cart')




from django.shortcuts import render

def payment_success(request):
    return render(request, 'store/payment_success.html')



