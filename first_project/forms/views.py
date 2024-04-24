from django.shortcuts import render
from forms.forms import UserForm, UserProfileInfoForm, NewUserForm

from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required
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

    return render(request, 'forms/form_page.html', {'form': form})


def users(request):
    form = NewUserForm()

    if request.method == 'POST':
        form = NewUserForm(request.POST)

        if form.is_valid():
            print("form is valid")
            form.save(commit=True)
            return index(request)  # after filling the form the user will go back to the home page
        else:
            print('ERROR, FORM IS NOT VALID')

    return render(request, 'forms/users.html', {'form': form})


def base(request):
    return render(request, 'forms/base.html')


def registration(request):
    registered = False
    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileInfoForm(data=request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)  # hashing the pwd
            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user  # creating the relationship between user and profile

            if 'profile_pic' in request.FILES:
                profile.profile_pic = request.FILES['profile_pic']

            profile.save()

            registered = True

        else:
            print(user_form.errors, profile_form.errors)
    else:
        user_form = UserForm()
        profile_form = UserProfileInfoForm()

    return render(request, 'forms/registration.html',
                  {'user_form': user_form,
                   'profile_form': profile_form,
                   'registered': registered})


def user_login(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request,username=username, password=password)

        if user:
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect(reverse('index'))
            else:
                return HttpResponse('Your account is not active.')
        else:
            print('Username or password is somehow invalid')
            print("username: {} and password: {}".format(username, password))
            return HttpResponse("Invalid login details supplied!")


    return render(request, 'forms/login.html',{})

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))