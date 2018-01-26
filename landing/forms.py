from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import *


class SubscriberForm(forms.ModelForm):
    class Meta:
        model = Subscriber
        exclude = [""]


class SignInForm(forms.ModelForm):
    class Meta:
        model = SignIn
        exclude = [""]




class SignUpForm(UserCreationForm):
    username = forms.CharField(max_length=30, required=True)
    phone = forms.CharField(max_length=30, required=False)

    class Meta:
        model = User
        fields = ('username', 'email','phone', 'password1', 'password2', )