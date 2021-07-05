from django.urls import path

from Login.api.views import *

app_name = "Login"

urlpatterns = [
    path("", logIn, name="api_login"),
    path("username/", userName, name="api_username"), 
    path("signup/", signUp, name="api_signup"), 
]
