from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, HttpResponseRedirect
from .forms import SignUpForm , EditUserProfileForm
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm


# signup view functions
def sign_up(request):
    if request.method == "POST":
        fm=SignUpForm(request.POST)
        if fm.is_valid():
            messages.success(request, 'Account created succesfully')
            fm.save()
    else:
        fm=SignUpForm()
    return render(request, 'enroll/signup.html', {'form':fm})

# login view function
def user_login(request):
    if not request.user.is_authenticated:
        if request.method =="POST":
            fm = AuthenticationForm(request=request, data=request.POST)
            if fm.is_valid():
                uname = fm.cleaned_data['username']
                upass = fm.cleaned_data['password']
                user = authenticate(username=uname, password=upass)
                if user is not None:
                    login(request, user)
                    messages.success(request,'logged in succesfully')
                    return HttpResponseRedirect('/profile/')
        else:
            fm = AuthenticationForm()
        return render(request,'enroll/userlogin.html', {'form':fm})
    else:
        return HttpResponseRedirect('/profile/')


# profile

def user_profile(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            fm=EditUserProfileForm(request.POST, instance = request.user)
            if fm.is_valid():
                messages.success(request, 'Profile Updated !!!')
                fm.save()
        else:
            fm = EditUserProfileForm(instance=request.user)
        fm = EditUserProfileForm(instance=request.user)
        return render(request, 'enroll/profile.html', {'name':request.user , 'form':fm})
    else:
        return HttpResponseRedirect('/login/')

# logout
def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/login/')