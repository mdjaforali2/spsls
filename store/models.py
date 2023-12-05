# models.py
from django.db import models
from django.contrib.auth.models import AbstractUser

class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Department(models.Model):
    name = models.CharField(max_length=50)
    
    def __str__(self):
        return self.name

class Position(models.Model):
    name = models.CharField(max_length=50)
    
    def __str__(self):
        return self.name

class CustomUser(AbstractUser):
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    city = models.CharField(max_length=255)

    DHAKA = 'DH'
    CHITTAGONG = 'CG'
    RAJSHAHI = 'RA'
    KHULNA = 'KH'
    BARISAL = 'BA'
    SYLHET = 'SY'
    RANGPUR = 'RN'

    DIVISION_CHOICES = [
        (DHAKA, 'Dhaka'),
        (CHITTAGONG, 'Chittagong'),
        (RAJSHAHI, 'Rajshahi'),
        (KHULNA, 'Khulna'),
        (BARISAL, 'Barisal'),
        (SYLHET, 'Sylhet'),
        (RANGPUR, 'Rangpur'),
    ]

    DIVISION_DEFAULT = CHITTAGONG

    division = models.CharField(max_length=2, choices=DIVISION_CHOICES, default=DIVISION_DEFAULT)

    CUSTOMER = 'customer'
    EMPLOYEE = 'employee'
    MANAGER = 'manager'
    SUPERVISOR = 'supervisor'
    HR = 'hr'
    COO = 'coo'

    ROLE_CHOICES = [
        (CUSTOMER, 'Customer'),
        (EMPLOYEE, 'Employee'),
        (MANAGER, 'Manager'),
        (SUPERVISOR, 'Supervisor'),
        (HR, 'Human Resources'),
        (COO, 'Chief Operating Officer'),
    ]

    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default=CUSTOMER)

    def save(self, *args, **kwargs):
        if not self.division:
            self.division = self.DIVISION_DEFAULT
        super().save(*args, **kwargs)

    def __str__(self):
        return self.username

from django.utils import timezone

class Employee(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    employee_id = models.AutoField(primary_key=True)    
    department = models.ForeignKey(Department, on_delete=models.SET_NULL, null=True, blank=True)
    position = models.ForeignKey(Position, on_delete=models.SET_NULL, null=True, blank=True)
    date_of_hiring = models.DateField(default=timezone.now)
    
    # Updated Fields
    EMPLOYEE_TYPE_CHOICES = [
        ('Part-Time', 'Part-Time'),
        ('Full-Time', 'Full-Time'),
        ('Contract', 'Contract'),
        ('Temporary', 'Temporary'),
    ]
    employee_type = models.CharField(max_length=20, choices=EMPLOYEE_TYPE_CHOICES, null=True)
    
    # If part-time, availability for each day of the week
    availability_monday_start = models.TimeField(null=True, blank=True)
    availability_monday_finish = models.TimeField(null=True, blank=True)
    
    availability_tuesday_start = models.TimeField(null=True, blank=True)
    availability_tuesday_finish = models.TimeField(null=True, blank=True)
    
    availability_wednesday_start = models.TimeField(null=True, blank=True)
    availability_wednesday_finish = models.TimeField(null=True, blank=True)
    
    availability_thursday_start = models.TimeField(null=True, blank=True)
    availability_thursday_finish = models.TimeField(null=True, blank=True)
    
    availability_friday_start = models.TimeField(null=True, blank=True)
    availability_friday_finish = models.TimeField(null=True, blank=True)
    
    availability_saturday_start = models.TimeField(null=True, blank=True)
    availability_saturday_finish = models.TimeField(null=True, blank=True)
    
    availability_sunday_start = models.TimeField(null=True, blank=True)
    availability_sunday_finish = models.TimeField(null=True, blank=True)
    
    hourly_rate = models.DecimalField(max_digits=10, decimal_places=2, default=120)
    
    SHIFT_CHOICES = [
        ('Morning', 'Morning'),
        ('Evening', 'Evening'),
    ]
    shift = models.CharField(max_length=20, choices=SHIFT_CHOICES, null=True, blank=True)

    def __str__(self):
        return f"{self.user.username} - {self.get_employee_type_display()}"
    
    @staticmethod
    def generate_employee_id():
        last_employee = Employee.objects.order_by('-employee_id').first()
        if last_employee:
            return last_employee.employee_id + 1
        else:
            return 10000001



class Manager(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, primary_key=True)
    department = models.ForeignKey(Department, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f"Manager - {self.user.username}"

class Supervisor(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, primary_key=True)
    department = models.ForeignKey(Department, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f"Supervisor - {self.user.username}"

class HR(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, primary_key=True)

    def __str__(self):
        return f"HR - {self.user.username}"

class COO(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, primary_key=True)

    def __str__(self):
        return f"COO - {self.user.username}"

class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    size = models.CharField(max_length=10, null=True, blank=True)
    color = models.CharField(max_length=20, null=True, blank=True)
    image = models.ImageField(upload_to='product_images/', null=True, blank=True)

    def __str__(self):
        return self.name
