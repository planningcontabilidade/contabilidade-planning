from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', views.home, name='home'),

    # Login padrão do Django (usa registration/login.html automaticamente)
    path('login/', auth_views.LoginView.as_view(), name='login'),

    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),

    path('create-user/', views.create_user, name='create_user'),
]
