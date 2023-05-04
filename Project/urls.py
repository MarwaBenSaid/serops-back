from django.urls import path
from .views import RetrieveAllView, RetrieveView, CreateView, UpdateView, DeleteView

urlpatterns = [
    path('all',RetrieveAllView.as_view()),
    path('<int:id>/',RetrieveView.as_view()),
    path('new',CreateView.as_view()),
    path('<int:id>/update/',UpdateView.as_view()),
    path('<int:id>/delete/',DeleteView.as_view())

]
