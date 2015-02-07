import inspect
import os
from datetime import timedelta, datetime
from django.shortcuts import render
import time
from discipline.models import Discipline
from dive_log.models import Session, Dive, DataPoint
from parser.omer import Omer
from parser.dictionary import get, put


def upload(request):
    example_data = 'omer-up-x1-2015-02-04-eriksdalsbadet-25m.csv'
    base_path = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe()))) + '/'
    test_file = os.path.join(base_path, '../parser/tests/data', example_data)
    omer = Omer(test_file)

    session = Session()
    session.date = get(omer.content, 'summary.date')
    session.time = datetime.strptime("19:00:00", "%H:%M:%S")
    session.save()

    time_of_dive = session.time

    for dive_entry in get(omer.content, 'dives'):
        dive = Dive()
        dive.session = session
        dive.discipline = Discipline.objects.get(abbreviation='DNF')
        t = datetime.strptime(get(dive_entry, 'summary.time.surface'), "%H:%M:%S")
        dive.rest_duration = timedelta(hours=t.hour, minutes=t.minute, seconds=t.second)
        t = datetime.strptime(get(dive_entry, 'summary.time.dive'), "%H:%M:%S")
        dive.dive_duration = timedelta(hours=t.hour, minutes=t.minute, seconds=t.second)
        dive.start = time_of_dive
        time_of_dive = time_of_dive + dive.rest_duration + dive.dive_duration
        dive.save()
        
        for point in get(dive_entry, 'data_points'):
            data_point = DataPoint()
            data_point.dive = dive
            data_point.second = get(point, 'item') - 1
            data_point.depth = get(point, 'depth')
            data_point.temperature = get(point, 'temp')
            data_point.heart_rate = get(point, 'hr')
            data_point.save()

    context = {
        'date':  get(omer.content, 'summary.date'),
        'dive_count': get(omer.content, 'summary.dive.count')
    }

    return render(request, 'done.html', context)