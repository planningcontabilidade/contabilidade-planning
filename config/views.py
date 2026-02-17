from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required


@login_required
def home(request):
    return render(request, "index.html")


def create_user(request):
    if not User.objects.filter(username="admin").exists():
        User.objects.create_superuser(
            "admin",
            "admin@email.com",
            "123456"
        )
    return render(request, "index.html")
