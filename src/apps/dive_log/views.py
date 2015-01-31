from django.shortcuts import render
from .models import Session, Dive


def list_sessions(request):
    sessions = Session.objects.all()
    context = {
        'sessions': sessions
    }

    return render(request, 'list.html', context)


def details(request, dive_id):
    dive = Dive.objects.get(id=dive_id)

    context = {
        'dive': dive
    }

    return render(request, 'details.html', context)