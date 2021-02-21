from django.shortcuts import render

# My views here.
def home(request):
    return render(request, 'Login_App/index.html')
