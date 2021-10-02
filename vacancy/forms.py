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
                attrs={'class': 'form-control'}),
            'written_cover_letter': forms.Textarea(
                attrs={'class': 'form-control'})
        }