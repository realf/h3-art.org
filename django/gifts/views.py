# Create your views here.
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
#from django.contrib.sessions.models import Session
from django.shortcuts import render_to_response, redirect
from django.template import RequestContext
from gifts.forms import GiftCreateForm
from gifts.models import Artifact

@login_required
def user_profile(request):
#    user = request.user
    return render_to_response('profile.html', {}, 
                              context_instance=RequestContext(request))    
    

@login_required
def new_gift(request, gift = ""):
    if request.method == 'POST':
        form = GiftCreateForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = User.objects.get(username=request.user.username)
            artifact = Artifact(name=cd['name'], 
                                description = cd['description'],
                                creator = user,
                                master = user,
                                owner = request.user,
                                status = 1)
            artifact.save()
            return redirect('/gifts/new/'+cd['name'])
    else:
        form = GiftCreateForm
    return render_to_response('new_gift.html', {'form': form, 'gift': gift}, 
                              context_instance=RequestContext(request))
    
def user_gifts(request):
    
    return render_to_response('user_gifts.html', {}, context_instance=RequestContext(request))


def my_gifts(request):
    return render_to_response('my_gifts.html', {}, context_instance=RequestContext(request))
    

def main(request):
    return render_to_response('index.html', {}, context_instance=RequestContext(request))  
  
