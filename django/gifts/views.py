# Create your views here.
import random, string
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
#from django.contrib.sessions.models import Session
from django.shortcuts import render_to_response, redirect, get_object_or_404
from django.template import RequestContext
from gifts.forms import GiftCreateForm, ArtifactCodeForm
from gifts.models import Artifact, Permissions, Quest


def rnd_str(rnd_len = 6):
    choice_set = string.ascii_letters + string.digits
    return "".join([random.choice(choice_set) for i in range(rnd_len)])



def user_profile(request, username):
    """Shows user profile page
    
    cont - context dictionary for next variables:
    cont['user_profile'] - User object for which profile should be shown
    cont['mastered_gifts'] - list of mastered gifts by user        
    """    
    
    cont = {}
    if username:
        # User is explicitly specified. Find user in DB.
        # return 404 Error if user not found
        cont['user_profile'] = get_object_or_404(User, username=username)
    elif request.user.is_authenticated():
        # User is not specified. Show current user profile page 
        # if user is authentificated or redirect to login page otherwise
        cont['user_profile'] = request.user        
    else:
        return redirect('django.contrib.auth.views.login')
    cont['mastered_gifts'] = cont['user_profile'].mastered_gifts.all()
    return render_to_response('profile.html', cont, 
                              context_instance=RequestContext(request))    
    

@login_required
def new_gift(request, gift = ""):
    if request.method == 'POST':
        form = GiftCreateForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = User.objects.get(username=request.user.username)
            artifact = Artifact.objects.create(name=cd['name'], 
                                description = cd['description'],
                                uid = rnd_str(6),
                                #masters = [user],
                                owner = request.user,
                                permissions = Permissions.objects.get(pk=1),
                                status = 1)
            artifact.masters = [user]
            artifact.creators = [user]
            #artifact.save()
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
    if request.method == 'POST':
        form = ArtifactCodeForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            
    else:
        artifact_code_form = ArtifactCodeForm       
    return render_to_response('main.html', 
                              {'artifact_code_form': artifact_code_form}, 
                              context_instance=RequestContext(request))  
  
