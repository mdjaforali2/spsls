from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView
from django.views.generic import TemplateView
from django.contrib.auth import views as auth_views
from .views import manage_product, view_cart, add_to_cart, update_cart, remove_from_cart, clear_cart



urlpatterns = [
    path('', views.main_page, name='main_page'),  # Main page URL should come first
    path('product/<int:product_id>/', views.product_detail, name='product_detail'),

    path('cart_/', view_cart, name='view_cart'),
    path('add_to_cart/<int:product_id>/', add_to_cart, name='add_to_cart'),
    path('update_cart/', update_cart, name='update_cart'),
    path('remove_from_cart/<int:product_id>/', remove_from_cart, name='remove_from_cart'),
    path('clear_cart/', clear_cart, name='clear_cart'),

    path('process_order/', views.process_order, name='process_order'),
    path('product_list/', views.product_list, name='product_list'),
    path('signup/', views.customer_signup, name='signup'),
    path('accounts/login/', views.login_view, name='login'),
    path('logout/', LogoutView.as_view(next_page='logout_success'), name='logout'),
    path('logout_success/', TemplateView.as_view(template_name='registration/logout.html'), name='logout_success'),

    # Password reset URLs with custom templates in the "registration" folder
    path('password_reset/', auth_views.PasswordResetView.as_view(template_name='registration/password_reset_form.html'), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='registration/password_reset_done.html'), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='registration/password_reset_confirm.html'), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='registration/password_reset_complete.html'), name='password_reset_complete'),

    path('add_product/', views.add_product, name='add_product'),
    path('add_file/', views.add_file, name='add_file'),
    path('manage_product/<int:product_id>/', manage_product, name='manage_product'),
    
    path('payment_success/', views.payment_success, name='payment_success'),


]


urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)