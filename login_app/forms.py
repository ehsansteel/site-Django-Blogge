from django import forms
from django.contrib.auth import authenticate
from django.forms import ValidationError
from django.contrib.auth.models import User



class LoginForms(forms.Form):
    username = forms.CharField(max_length=75, widget=forms.TextInput(attrs={"class": 'form-control', "placeholder": 'username'}))
    Password = forms.CharField(widget=forms.PasswordInput(attrs={"class": 'form-control', "placeholder": 'password'}))




    def clean_Password(self):
        users = authenticate(usrename=self.cleaned_data.get("username"), Password=self.cleaned_data.get("Password"))
        if users is not True:
            return self.cleaned_data.get("Password")
        raise ValidationError("The information entered is not correct. Please try again", code="invalid_info")



class UserEditForms(forms.ModelForm):
    class Meta:
        model = User
        fields = ("first_name", "last_name", "username", "password", "email")


