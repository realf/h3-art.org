# Create your views here.
'''
Created on 09.06.2012

@author: realf
'''

from django.shortcuts import render_to_response, redirect
from django.template import RequestContext
from users.forms import RegistrationForm
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password

# A very simple registration view. 
# TODO: Needs to be tested properly. Also the template should be revised. 
def register(request):
    # If user is authenticated no need to register
    if User.is_authenticated:
        return redirect("/accounts/profile/")
    
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            # User must agree with Terms of Service
            if (cd['acceptTheTOS'] == True):
                newUser = User(username=cd['username'], email=cd['email'], password=make_password(cd['password']))
                # Currently we don't require the user validation by email so make him active at once
                newUser.is_active = True;
                newUser.save()
                # Now we can proceed with login
                return redirect("/accounts/login/")
            else:
                # TODO: make the error to be displayed in template
                errors = "You must agree..." 
                return render_to_response("register.html", {'form': form, 'errors': errors}, context_instance=RequestContext(request))
        else:
            errors = form.errors
            return render_to_response("register.html", {'form': form, 'errors': errors}, context_instance=RequestContext(request))
    
    form = RegistrationForm()
    return render_to_response("register.html", {'form': form}, context_instance=RequestContext(request))
