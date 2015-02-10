import StringIO
from datetime import datetime
from django.shortcuts import render, redirect
from .forms import UploadFileForm
from .models import Session, Dive, DataPoint
from parser.omer import Omer
from uploader.views import add_omer_file_to_db


def list_sessions(request, username):
    sessions = Session.objects.filter(user__username=username)
    context = {
        'sessions': sessions,
        'username': username
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

    return render(request, 'chart.html', context)


def create(request):
    if request.method == 'GET':
        return render(request, 'create.html')


def upload(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)

        if form.is_valid():
            handle_uploaded_file(request.FILES['file'], request.user.id, request.POST['session_start'], request.POST['discipline'])
            return redirect('list_sessions', request.user.username)

    else:
        form = UploadFileForm()
    return render(request, 'create.html', {'form': form})


def handle_uploaded_file(f, user_id, session_start, discipline):
    output = StringIO.StringIO()
    for chunk in f.chunks():
        output.write(unicode(chunk, "utf-16"))

    session_time = datetime.strptime(session_start, "%H:%M")

    omer = Omer()
    omer.read_stream(output)

    add_omer_file_to_db(omer, user_id, session_time, discipline)

    print output.len, output