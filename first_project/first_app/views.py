
from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    index_dict = {'insert_index': "this is the index page and there's an index"}
    return render(request, 'first_app/index.html', context=index_dict)
def help(request):
    help_dict = {'insert_help': "this is the help page and there's an help"}
    return render(request,'first_app/help.html',context=help_dict)
