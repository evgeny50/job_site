from django import forms

from .models import Company


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