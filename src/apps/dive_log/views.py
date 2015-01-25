from django.shortcuts import render
from .models import Session


def list_sessions(request):
    sessions = Session.objects.all()
    context = {
        'sessions': sessions
    }

    return render(request, 'list.html', context)