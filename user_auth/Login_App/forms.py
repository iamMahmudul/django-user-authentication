from django import forms
from django.contrib.auth.models import User
from Login_App.models import UserInformation

#Forms here

class UserForm(forms.ModelForm):
    class Meta():
        model = User
        fields = ('username', 'email', 'password')

class UserInformationForm(forms.ModelForm):
    class Meta():
        model = UserInformation
        fields = ('facebook_id', 'profile_pic')
