from django import forms

from .models import Resume


class CreateResume(forms.ModelForm):

    class Meta:
        model = Resume
        fields = ('first_name', 'title', 'second_name', 'status', 'salary',
                  'specialty', 'grade', 'education', 'experience', 'portfolio')
        widgets = {
            'first_name': forms.TextInput(attrs={
                'class': 'form-control',
                'readonly': True
            }),
            'title': forms.TextInput(attrs={
                'class': 'form-control'
            }),
            'second_name': forms.TextInput(attrs={
                'class': 'mb-2 text-dark form-control',
                'readonly': True
            }),
            'status': forms.Select(attrs={
                'class': 'mb-2 text-dark custom-select mr-sm-2'
            }),
            'salary': forms.NumberInput(attrs={
                'class': 'mb-2 text-dark form-control'
            }),
            'specialty': forms.Select(attrs={
                'class': 'mb-2 text-dark custom-select mr-sm-2'
            }),
            'grade': forms.Select(attrs={
                'class': 'mb-2 text-dark custom-select mr-sm-2'
            }),
            'education': forms.Textarea(attrs={
                'class': 'mb-2 text-dark form-control text-uppercase',
                'rows': 4
            }),
            'experience': forms.Textarea(attrs={
                'class': 'mb-2 text-dark form-control',
                'rows': 4
            }),
            'portfolio': forms.TextInput(attrs={
                'class': 'mb-2 text-dark form-control'
            })
        }
