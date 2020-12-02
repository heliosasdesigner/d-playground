from django.shortcuts import render



# Create your views here.
def index(request):
    context_dict = {'text':'Hello world from index','number':427891,'text_2':'Hello, Here is testing words and Hello world'}
    return render(request, 'appone/index.html',context_dict) # need to put the contect_dict after , 'appone/index.html'

def other(request):
    return render(request, 'appone/other.html')

def relative(request):
    return render(request, 'appone/relative_url_templates.html')