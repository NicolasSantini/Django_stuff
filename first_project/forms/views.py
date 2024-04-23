from django.shortcuts import render
from . import forms
# Create your views here.

def index(request):
    return render(request, 'forms/index.html')

def form(request):
    form = forms.FormName()

    if request.method == 'POST':
        form = forms.FormName(request.POST)
        if form.is_valid():
            print("form is valid")
            print("NAME: " + form.cleaned_data['name'])
            print("EMAIL: " + form.cleaned_data['email'])
            print("TEXT: " + form.cleaned_data['text'])


    return render(request,'forms/form_page.html',{'form':form})
