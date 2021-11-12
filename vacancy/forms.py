from django import forms
from django.contrib.auth.models import User

from resume.models import Resume
from .models import Application, Vacancy


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


class SendCoverLetterForm(forms.ModelForm):

    class Meta:
        model = Application
        fields = ('written_cover_letter',)
        widgets = {
            'written_cover_letter': forms.Textarea(
                attrs={'class': 'form-control'}
            )
        }

    def __init__(self, pk, *args, **kwargs):
        super(SendCoverLetterForm, self).__init__(*args, **kwargs)
        self.fields['resume'] = forms.ModelChoiceField(
            queryset=Resume.objects.filter(user_id=pk),
            widget=forms.Select(
                attrs={'class': 'form-control'}
            ))



class SearchForm(forms.Form):
    q = forms.CharField(
        max_length=255,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control mr-sm-2 mx-auto',
                'type': 'text',
                'value': 'Backend',
            }
        )
    )


class HomeSearchForm(forms.Form):
    q = forms.CharField(
        max_length=255,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control w-100',
                'type': 'search',
                'placeholder': 'Find a job or internship',
            }
        )
    )
