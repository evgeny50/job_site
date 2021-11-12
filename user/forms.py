from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
# from django.contrib.auth.models import User

from user.models import CustomUser


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
        model = CustomUser
        fields = ['username', 'password1', 'password2']


class FormRegisterEmployer(UserCreationForm):
    first_name = forms.CharField(
        label='First name',
        widget=forms.TextInput(
            attrs={'class': 'form-control'}
        )
    )
    last_name = forms.CharField(
        label='Last_name',
        widget=forms.TextInput(
            attrs={'class': 'form-control'}
        )
    )
    phone_number = forms.CharField(
        label='Phone',
        widget=forms.NumberInput(
            attrs={'class': 'form-control',
                   'placeholder': '+7 (999) 999-99-99'}
        )
    )

    password1 = forms.CharField(
        label='Password',
        widget=forms.PasswordInput(
            attrs={'class': 'form-control'}
        )
    )
    password2 = forms.CharField(
        label='Repeat password',
        widget=forms.PasswordInput
        (attrs={'class': 'form-control'})
    )

    class Meta:
        model = CustomUser
        fields = ['first_name', 'last_name', 'phone_number', 'password1', 'password2']


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