from dataclasses import field
from pyexpat import model
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class BlogPostForm(forms.Form):
    title = forms.CharField(max_length=300)
    subtitle = forms.CharField(max_length=900)
    content = forms.CharField(max_length=10000)
    category = forms.CharField(max_length=45)

class ContactMessageForm(forms.Form):
    name = forms.CharField(max_length=30)
    lastname = forms.CharField(max_length=30)
    message = forms.CharField(max_length=700)

class TeamMemberForm(forms.Form):
    name = forms.CharField(max_length=30)
    lastname = forms.CharField(max_length=30)
    email = forms.EmailField()
    githubaccount = forms.CharField(max_length=30)

class UserRegisterForm(UserCreationForm):
    email=forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        help_texts = {k:"" for k in fields}

class UserUpdateForm(UserCreationForm):
    email=forms.EmailField()
    password1=forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2=forms.CharField(label='Repetir contraseña', widget=forms.PasswordInput)

    fistname= forms.CharField(label='Nombre')
    lastname= forms.CharField(label='Apellido')

    class Meta:
        model = User
        fields = ['email', 'password1', 'password2', 'fistname', 'lastname']
        help_texts = {k:"" for k in fields}