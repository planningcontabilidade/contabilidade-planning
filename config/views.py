from django.contrib.auth.models import User

def create_user(request):
    if not User.objects.filter(username='admin').exists():
        User.objects.create_superuser('admin', 'admin@email.com', '123456')
    return render(request, "index.html")
