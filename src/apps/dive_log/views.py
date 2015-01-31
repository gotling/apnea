from django.shortcuts import render
from .models import Session, Dive, DataPoint


def list_sessions(request):
    sessions = Session.objects.all()
    context = {
        'sessions': sessions
    }

    return render(request, 'list.html', context)


def details(request, dive_id):
    dive = Dive.objects.get(id=dive_id)

    data_points = DataPoint.objects.filter(dive_id=dive_id).values_list('second', 'depth', 'heart_rate')

    time, depth, heart_rate = zip(*data_points)

    context = {
        'dive': dive,
        'time': [t for t in time],
        'depth': [float(d) for d in depth],
        'heart_rate': [hr for hr in heart_rate]
    }

    return render(request, 'chart2.html', context)