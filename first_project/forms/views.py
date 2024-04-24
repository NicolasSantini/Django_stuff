from django.shortcuts import render
from . import forms
from forms.forms import NewUserForm
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



def users(request):
    form = NewUserForm()

    if request.method == 'POST':
        form = NewUserForm(request.POST)

        if form.is_valid():
            print("form is valid")
            form.save(commit=True)
            return index(request) #after filling the form the user will go back to the home page
        else:
            print('ERROR, FORM IS NOT VALID')

    return render(request,'forms/users.html',{'form':form})
