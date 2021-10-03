from django import forms

from .models import Application


class SendCoverLetterForm(forms.ModelForm):
    class Meta:
        model = Application
        fields = ('written_username', 'written_phone', 'written_cover_letter')
        widgets = {
            'written_username': forms.TextInput(
                attrs={'class': 'form-control'}),
            'written_phone': forms.NumberInput(
                attrs={'class': 'form-control',
                       'type': 'tel'}),
            'written_cover_letter': forms.Textarea(
                attrs={'class': 'form-control'})
        }


class SearchForm(forms.Form):
    q = forms.CharField(max_length=255,
                        widget=forms.TextInput(
                            attrs={
                                    'class': 'form-control mr-sm-2 mx-auto',
                                    'type': 'text',
                                    'value': 'Backend'}))


class HomeSearchForm(forms.Form):
    q = forms.CharField(max_length=255,
                        widget=forms.TextInput(
                            attrs={'class': 'form-control w-100',
                                   'type': 'search',
                                   'placeholder': 'Find a job or internship',
                                   }
                        ))
