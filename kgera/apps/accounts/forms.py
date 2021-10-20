from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.forms import widgets
from .models import User


ADMIN = 1
SEC = 2
BASIC = 3

USERTYPE_CHOICES = (
    (ADMIN, ('Administrator')),
    (SEC, ('Secretary')),
    (BASIC, ('Basic User')),
)

class LoginForm(forms.Form):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder" : "Username",                
                "class": "input100"
            }
        ))
    
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "placeholder" : "Password",                
                "class": "input100"
            }
        ))

class NewUserForm(UserCreationForm):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder" : "Username",                
                "class": "form-control"
            }
        ))
    email = forms.EmailField(
        widget=forms.EmailInput(
            attrs={
                "placeholder" : "Email",                
                "class": "form-control"
            }
        ))

    usertype = forms.ChoiceField(
        choices=USERTYPE_CHOICES,
        
    )

    password1 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "placeholder" : "Password",                
                "class": "form-control"
            }
        ))
    password2 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "placeholder" : "Password check",                
                "class": "form-control"
            }
        ))

    class Meta:
        model = User
        fields = ('username', 'email', 'usertype', 'password1', 'password2')