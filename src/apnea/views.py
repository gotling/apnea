from django.contrib.auth.models import User
from django.shortcuts import render


def home(request):
    users = User.objects.all()
    context = {
        'users': users
    }

    return render(request, 'home.html', context)