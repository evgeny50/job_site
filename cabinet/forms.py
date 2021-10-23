from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

from vacancy.models import Company, Vacancy


class FormRegisterUser(UserCreationForm):
    username = forms.CharField(
        label='Username',
        widget=forms.TextInput
        (attrs={'class': 'form-control'})
    )
    password1 = forms.CharField(
        label='Password',
        widget=forms.PasswordInput
        (attrs={'class': 'form-control'})
    )
    password2 = forms.CharField(
        label='Repeat password',
        widget=forms.PasswordInput
        (attrs={'class': 'form-control'})
    )

    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']


class FormLoginUser(AuthenticationForm):
    username = forms.CharField(
        label='Username',
        widget=forms.TextInput
        (attrs={'class': 'form-control'})
    )
    password = forms.CharField(
        label='Password',
        widget=forms.PasswordInput
        (attrs={'class': 'form-control'})
    )


class FormCreateCompany(forms.ModelForm):

    class Meta:
        model = Company
        fields = ['name', 'city', 'logo', 'employee_count', 'description']
        widgets = {
            'name': forms.TextInput(
                attrs={'class': 'form-control'}
            ),
            'city': forms.TextInput(
                attrs={'class': 'form-control'}
            ),
            'logo': forms.FileInput(
                attrs={'class': 'form-control', 'style': 'display: none;'}
            ),
            'employee_count': forms.NumberInput(
                attrs={'class': 'form-control', 'min': 0}
            ),
            'description': forms.Textarea(
                attrs={'class': 'form-control', 'rows': 4}
            )
        }


class FormCreateVacancy(forms.ModelForm):

    class Meta:
        model = Vacancy
        fields = ['title', 'salary_min',
                  'salary_max', 'specialty', 'description', 'skills']
        widgets = {
            'title': forms.TextInput(
                attrs={'class': 'form-control'}
            ),
            'specialty': forms.Select(
                attrs={'class': 'custom-select mr-sm-2'}
            ),
            'salary_min': forms.TextInput(
                attrs={'class': 'form-control'}
            ),
            'salary_max': forms.TextInput(
                attrs={'class': 'form-control'}
            ),
            'skills': forms.SelectMultiple(
                attrs={'class': 'form-control', 'rows': 2}
            ),
            'description': forms.Textarea(
                attrs={'class': 'form-control', 'rows': 5}
            )
         }
