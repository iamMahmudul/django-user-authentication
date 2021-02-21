from django.shortcuts import render
from Login_App.forms import UserForm, UserInformationForm

# My views here.
def home(request):
    return render(request, 'Login_App/index.html')

def register(request):
    user_form = UserForm()
    user_info_form = UserInformationForm()
    dict = {'user_form':user_form, 'user_info_form':user_info_form}
    return render(request,'Login_App/register.html', context = dict)
