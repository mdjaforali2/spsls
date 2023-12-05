# employee_management/forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm
from store.models import Employee, CustomUser
from django.forms.widgets import DateInput, TimeInput


class CustomUserSignUpForm(UserCreationForm):
    phone_number = forms.CharField(max_length=15, required=True)
    city = forms.CharField(max_length=255, required=True)
    division = forms.ChoiceField(choices=CustomUser.DIVISION_CHOICES, initial=CustomUser.DIVISION_DEFAULT)
    role = forms.ChoiceField(choices=CustomUser.ROLE_CHOICES, initial=CustomUser.CUSTOMER)

    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'password1', 'password2', 'phone_number', 'city', 'division', 'role']


class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ['employee_type', 'department', 'position', 'date_of_hiring', 'hourly_rate', 'shift']
        widgets = {
            'date_of_hiring': DateInput(attrs={'type': 'date'}),
        }
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Set the initial value for hourly_rate
        self.fields['hourly_rate'].initial = 120  # Replace 120 with your default value



# employee_management/forms.py
from django import forms
from store.models import Employee
from django.forms.widgets import TimeInput

class AvailabilityForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = [
            'availability_monday_start', 'availability_monday_finish',
            'availability_tuesday_start', 'availability_tuesday_finish',
            'availability_wednesday_start', 'availability_wednesday_finish',
            'availability_thursday_start', 'availability_thursday_finish',
            'availability_friday_start', 'availability_friday_finish',
            'availability_saturday_start', 'availability_saturday_finish',
            'availability_sunday_start', 'availability_sunday_finish',
        ]
        widgets = {
            'availability_monday_start': TimeInput(attrs={'type': 'time'}),
            'availability_monday_finish': TimeInput(attrs={'type': 'time'}),
            'availability_tuesday_start': TimeInput(attrs={'type': 'time'}),
            'availability_tuesday_finish': TimeInput(attrs={'type': 'time'}),
            'availability_wednesday_start': TimeInput(attrs={'type': 'time'}),
            'availability_wednesday_finish': TimeInput(attrs={'type': 'time'}),
            'availability_thursday_start': TimeInput(attrs={'type': 'time'}),
            'availability_thursday_finish': TimeInput(attrs={'type': 'time'}),
            'availability_friday_start': TimeInput(attrs={'type': 'time'}),
            'availability_friday_finish': TimeInput(attrs={'type': 'time'}),
            'availability_saturday_start': TimeInput(attrs={'type': 'time'}),
            'availability_saturday_finish': TimeInput(attrs={'type': 'time'}),
            'availability_sunday_start': TimeInput(attrs={'type': 'time'}),
            'availability_sunday_finish': TimeInput(attrs={'type': 'time'}),
        }
