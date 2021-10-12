from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate
from django import forms
from .models import User


class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = (
        'firstname', 'lastname', 'username', 'email', 'phone_number', 'country', 'haveshop', 'password1', 'password2')


class LoginForm(forms.ModelForm):
    password = forms.CharField(label='Password', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username', 'password')

    def clean(self):
        if self.is_valid():
            username = self.cleaned_data['username']
            password = self.cleaned_data['password']
            if not authenticate(username=username, password=password):
                raise forms.ValidationError("Invalid login")


class ProfileEdit(forms.ModelForm):
    class Meta:
        model = User
        fields = ('firstname', 'lastname', 'username', 'email', 'phone_number', 'country', 'hide_information')
