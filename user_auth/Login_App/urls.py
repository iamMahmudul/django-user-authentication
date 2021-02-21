from django.conf.urls import url
from django.urls import path, include
from . import views


app_name = 'Login_App'
urlpatterns = [
    path('', views.home, name = 'home'),
    path('register/', views.register, name = 'register'),
]
