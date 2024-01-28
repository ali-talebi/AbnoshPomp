from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class SignUpForm(UserCreationForm):
    email = forms.CharField(max_length=254, required=True, widget=forms.EmailInput())
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

class Search_Form(forms.Form) : 

    text = forms.CharField()



class Login_Form(forms.Form) : 

    username = forms.CharField()
    password = forms.CharField()
    

    