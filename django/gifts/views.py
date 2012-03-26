# Create your views here.
#from django.core.context_processors import csrf
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.template import RequestContext
from gifts.forms import GiftCreateForm

def new_gift(request):
    #var_dict = {}
    #var_dict.update(csrf(request))
    #assert False
    if request.method == 'POST':
        form = GiftCreateForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            #assert False
            return HttpResponseRedirect(reverse('gifts.views.user_gifts'))
    else:
        form = GiftCreateForm
    #var_dict['form'] = form
    return render_to_response('new_gift.html', {'form': form}, 
                              context_instance=RequestContext(request))
    
def user_gifts(request):
    return render_to_response('user_gifts.html', {})
  
  
