from django import forms
from .models import Contact
from django.core.exceptions import ValidationError

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ('name','phone','title','message')
        labels = {
            'name': (''),
            'phone': (''),
            'title': (''),
            'message': (''),
        }
        widgets = {
            'name': forms.TextInput(attrs={'placeholder':'نام شما','class':'name'}),
            'phone': forms.TextInput(attrs={'placeholder':'شماره تماس','class':'phone'}),
            'title': forms.TextInput(attrs={'placeholder':'موضوع','class':'title'}),
            'message': forms.Textarea(attrs={'placeholder':'پیام شما','class':'message'}),
        }