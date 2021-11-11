from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User


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