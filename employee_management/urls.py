# employee_management/urls.py
from django.urls import path
from .views import (
    employee_list,
    employee_detail,
    employee_create,
    employee_update,
    employee_delete,
    update_availability
)

urlpatterns = [
    path('employees/', employee_list, name='employee_list'),
    path('employees/<int:employee_id>/', employee_detail, name='employee_detail'),
    path('employees/create/', employee_create, name='employee_create'),
    path('employees/<int:employee_id>/update/', employee_update, name='employee_update'),
    path('employees/<int:employee_id>/delete/', employee_delete, name='employee_delete'),
    path('update_availability/<int:employee_id>/', update_availability, name='update_availability'),
]
