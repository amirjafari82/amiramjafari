from django import forms
from django.core.exceptions import ValidationError

class ProjectRequestForm(forms.Form):
    fname = forms.CharField(max_length=20,label='نام',required=True)
    lname = forms.CharField(max_length=20,label='نام خانوادگی',required=True)
    title = forms.CharField(max_length=50,label='موضوع سایت (میخواهید سایت شما در مورد چه چیزی باشد؟)',help_text='مثال: سایت فروشگاهی',required=True)
    desc = forms.CharField(label='توضیحات',widget=forms.Textarea(),required=True)
    phone = forms.CharField(max_length=11,label='شماره تماس',required=True,widget=forms.TextInput(attrs={'minlength':'11'}))
    
    def clean_phone(self):
        phone = self.cleaned_data.get('phone')
        if len(phone) < 11:
            print(len(phone))
            raise ValidationError("شماره تماس باید 11 رقم باشد.")
        return phone