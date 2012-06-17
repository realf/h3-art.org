# Create your views here.
'''
Created on 09.06.2012

@author: realf
'''

from django.shortcuts import render, redirect
from django.contrib.auth.views import redirect_to_login
from users.forms import RegistrationForm
from django.contrib.auth.decorators import login_required
    
@login_required
def user_profile(request):
    return render(request, 'profile.html', {})  

# A very simple registration view. 
# TODO: Needs to be tested properly. Also, the template should be revised. 
def register(request):
    if request.user.is_authenticated():
        return redirect("/accounts/profile/")
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return redirect_to_login("/accounts/profile/")
        else:
            return render(request, "register.html", {'form': form})
    form = RegistrationForm()
    return render(request, "register.html", {'form': form})
    