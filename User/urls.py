from django.contrib import admin
from django.urls import path

from .views import (Register,Login,Logout,activeUser)
urlpatterns = [
    path('register', Register.as_view()),
    path('login', Login.as_view()),
    path('user', activeUser.as_view()),
    path('logout', Logout.as_view())
    
]
