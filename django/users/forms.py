'''
Created on 09.06.2012

@author: realf
'''

from django import forms
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _

# A very simple form for user registration
# TODO: Seems it works, but it must be tested carefully.
class RegistrationForm(forms.ModelForm):
    """
    A form that creates a user, with no privileges, from the given username, email and
    password.
    """
    error_messages = {
        'duplicate_username': _("A user with that username already exists."),
        'duplicate_email': _("A user with that email already exists."),
        'rejected_TOS': _("You must accept our Terms of Service to join us."),
    }
    username = forms.RegexField(label=_("Username"), max_length=30,
        regex=r'^[\w.@+-]+$',
        help_text = _("Required. 30 characters or fewer. Letters, digits and "
                      "@/./+/-/_ only."),
        error_messages = {
            'invalid': _("This value may contain only letters, numbers and "
                         "@/./+/-/_ characters.")})
    password = forms.CharField(label=_("Choose a password"), min_length=6,
        widget=forms.PasswordInput)
    email = forms.EmailField(label=_("Your email"), help_text = _("We will never share your email address with third parties."))
    accept_TOS = forms.BooleanField(required = False, 
        label = _("I accept the TOS"), 
        help_text = _("You must accept our Terms of Service."))

    class Meta:
        model = User
        fields = ("username", "email",)

    def clean_username(self):
        # Since User.username is unique, this check is redundant,
        # but it sets a nicer error message than the ORM. See #13147.
        username = self.cleaned_data["username"]
        try:
            User.objects.get(username=username)
        except User.DoesNotExist:
            return username
        raise forms.ValidationError(self.error_messages['duplicate_username'])
    
    def clean_email(self):
        # We require email to be unique, so we must check it here
        email = self.cleaned_data["email"]
        try:
            User.objects.get(email=email)
        except User.DoesNotExist:
            return email
        raise forms.ValidationError(self.error_messages['duplicate_email'])
    
    def clean_accept_TOS(self):
        accept_TOS = self.cleaned_data['accept_TOS']
        if accept_TOS != True:
            raise forms.ValidationError(self.error_messages['rejected_TOS'])
    
    def save(self, commit=True):
        user = super(RegistrationForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user