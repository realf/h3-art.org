from django import forms

class ContactForm(forms.Form):
    subject = forms.CharField()
    email = forms.EmailField(required=False)
    message = forms.CharField()
  
class GiftCreateForm(forms.Form):
    name = forms.CharField()
    description = forms.CharField()