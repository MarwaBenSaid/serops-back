from django.contrib import admin
from django.urls import path , include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('Users.urls')),
    path('projects/', include('Projects.urls')),
    path('servers/', include('Servers.urls')),
]
