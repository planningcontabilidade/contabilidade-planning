from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib import messages


@login_required
def home(request):
    return render(request, "index.html")


def create_user(request):
    if not User.objects.filter(username="admin").exists():
        User.objects.create_superuser(
            username="admin",
            email="admin@email.com",
            password="123456"
        )
        messages.success(request, "Usuário admin criado com sucesso!")
    else:
        messages.info(request, "Usuário admin já existe.")

    return redirect("login")
