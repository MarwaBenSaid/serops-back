from django.urls import path
from .views import RetrieveAllView, RetrieveView, CreateView, UpdateView, DeleteView

urlpatterns = [
    path('all',RetrieveAllView.as_view()),
    path('<int:id>/',RetrieveView.as_view()),
    path('new',CreateView.as_view()),
    path('update/<int:id>',UpdateView.as_view()),
    path('delete/<int:id>',DeleteView.as_view())

]
