from django.urls import path
from .views import ActiveView, LogoutView, RegisterView, LoginView

urlpatterns = [
    path('login',LoginView.as_view()),
    path('register',RegisterView.as_view()),
    path('logout',LogoutView.as_view()),
    path('profile',ActiveView.as_view())

]
