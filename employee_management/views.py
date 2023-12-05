# employee_management/views.py
from django.shortcuts import render, get_object_or_404, redirect
from store.models import Employee
from django.contrib.auth import login
from .forms import CustomUserSignUpForm, EmployeeForm, AvailabilityForm

def employee_list(request):
    employees = Employee.objects.all()
    for employee in employees:
        print(f"id: {employee.employee_id}, Type: {employee.get_employee_type_display()}")
    return render(request, 'employee_management/employee_list.html', {'employees': employees})


def employee_detail(request, employee_id):
    employee = get_object_or_404(Employee, pk=employee_id)
    return render(request, 'employee_management/employee_detail.html', {'user': employee.user, 'employee': employee})

from django.contrib import messages

def employee_create(request):
    print('Entering employee_create')
    if request.method == 'POST':
        user_form = CustomUserSignUpForm(request.POST)

        if user_form.is_valid():
            user = user_form.save()
            
            # Generate employee_id
            employee_id = Employee.generate_employee_id()

            # Create Employee with generated employee_id
            Employee.objects.create(user=user, employee_id=employee_id)

            login(request, user, backend='django.contrib.auth.backends.ModelBackend')

            # Add a success message
            messages.success(request, 'Employee signed up successfully!')

            return redirect('employee_list')  # Redirect to the employee list page or another page
    else:
        user_form = CustomUserSignUpForm()

    return render(request, 'employee_management/employee_form.html', {'user_form': user_form})


def employee_update(request, employee_id):
    employee = get_object_or_404(Employee, pk=employee_id)

    if request.method == 'POST':
        employee_form = EmployeeForm(request.POST, instance=employee)

        employee_form.save()
        return redirect('employee_list')  # Redirect to the employee list page or another page
    else:
        employee_form = EmployeeForm(instance=employee)

    return render(request, 'employee_management/employee_update.html', { 'employee_form': employee_form, 'employee_id': employee_id})


def employee_delete(request, employee_id):
    employee = get_object_or_404(Employee, pk=employee_id)
    employee.delete()
    return redirect('employee_list')




def update_availability(request, employee_id):
    employee = get_object_or_404(Employee, pk=employee_id)

    if request.method == 'POST':
        availability_form = AvailabilityForm(request.POST, instance=employee)
        if availability_form.is_valid():
            availability_form.save()
            return redirect('employee_list')  # Redirect to the employee list page or another page
    else:
        availability_form = AvailabilityForm(instance=employee)

    return render(request, 'employee_management/update_availability.html', {'availability_form': availability_form, 'employee_id': employee_id})
