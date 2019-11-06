from django import forms
from .models import *
from django.core.exceptions import ValidationError


class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactAs
        fields = [
            'name',
            'email',
            'message'
        ]

        widgets = {
            'name': forms.TextInput(attrs={'class': 'input100', 'placeholder': 'Name'}),
            'email': forms.TextInput(attrs={'class': 'input100', 'placeholder': 'Email'}),
            'message': forms.Textarea(attrs={'class': 'input100', 'placeholder': 'Your Message'}),

        }

