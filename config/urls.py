from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),

    # Home protegida
    path('', views.home, name='home'),

    # Auth padrão Django (usa templates/registration/login.html)
    path('login/', auth_views.LoginView.as_view(
        template_name='registration/login.html'
    ), name='login'),

    path('logout/', auth_views.LogoutView.as_view(
        next_page='login'
    ), name='logout'),

    # Criar usuário
    path('create-user/', views.create_user, name='create_user'),
]
