# Create your views here.
from django.shortcuts import render_to_response, redirect
from django.template import RequestContext
from gifts.forms import GiftCreateForm

def new_gift(request, gift = ""):
    if request.method == 'POST':
        form = GiftCreateForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            return redirect('/gifts/new/'+cd['name'])
    else:
        form = GiftCreateForm
    return render_to_response('new_gift.html', {'form': form, 'gift': gift}, 
                              context_instance=RequestContext(request))
    
def user_gifts(request):
    return render_to_response('user_gifts.html', {}, context_instance=RequestContext(request))


def main(request):
    return render_to_response('index.html', {}, context_instance=RequestContext(request))  
  
