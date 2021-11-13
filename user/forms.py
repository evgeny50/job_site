from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

from phonenumber_field.formfields import PhoneNumberField

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
    phone_number = PhoneNumberField(
        label='Phone',
        widget=forms.NumberInput(
            attrs={'class': 'form-control'})
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
        fields = [
            'first_name', 'last_name', 'phone_number',
            'password1', 'password2'
        ]


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


class FormEditProfile(forms.ModelForm):
    first_name = forms.CharField(
        max_length=255,
        label='First name',
        widget=forms.TextInput
        (attrs={'class': 'form-control'})
    )
    last_name = forms.CharField(
        max_length=255,
        label='Last name',
        widget=forms.TextInput
        (attrs={'class': 'form-control'})
    )
    email = forms.EmailField(
        label='Email',
        widget=forms.EmailInput
        (attrs={'class': 'form-control'})
    )
    phone_number = PhoneNumberField(
        label='Phone',
        widget=forms.NumberInput(
            attrs={'class': 'form-control'})
    )

    class Meta:
        model = CustomUser
        fields = ['first_name', 'last_name', 'email', 'phone_number']
