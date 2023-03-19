from django.contrib import admin
from django.urls import path

from .views import (Register,Login,Logout)
urlpatterns = [
    path('register', Register.as_view()),
    path('login', Login.as_view()),
    path('logout', Logout.as_view())
    
]
