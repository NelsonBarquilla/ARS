from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from web.models import Employee
from employee.models import Profile



class EmployeeCreateForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = Employee
        fields = ['username', 'first_name', 'middle_name', 'last_name', 'emp_email',
                  'address', 'designation', 'department']


class EmployeeChangeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ['first_name', 'middle_name', 'last_name', 'emp_email',
                  'address', 'designation', 'department']


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image']
