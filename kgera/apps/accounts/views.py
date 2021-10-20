from django.shortcuts import render

########################

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.forms.utils import ErrorList
from django.http import HttpResponse
from .forms import LoginForm, NewUserForm

from .models import User

def login_view(request):
    form = LoginForm(request.POST or None)

    msg = None

    if request.method == "POST":

        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect("dashboard")
            else:    
                msg = 'Invalid credentials'    
        else:
            msg = 'Error validating the form'    

    return render(request, "accounts/login.html", {"form": form, "msg" : msg})


def user_profile(request):
    return render(request, 'accounts/profile.html')
