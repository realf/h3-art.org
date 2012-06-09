'''
Created on 09.06.2012

@author: realf
'''

from django import forms

# A very simple form for user registration
# TODO: Seems it works, but must be tested carefully.
class RegistrationForm(forms.Form):
    username = forms.CharField(max_length=30)
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput, min_length=6)
    acceptTheTOS = forms.BooleanField(required=False)