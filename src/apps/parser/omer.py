# coding: utf-8
import re
import codecs

from .dictionary import get, put

summary_key_conversion = {
    "Date": 'date',
    "No. of dives": 'dive.count',
    "Total time": 'time.total',
    "Total dive time": 'time.dive.total',
    "Total surface time": 'time.surface',
    "Average dive time": 'time.dive.average',
    "Maximum dive time": 'time.dive.max',
    "Maximum depth": 'depth.max',
    "Average depth": 'depth.average',
    "Maximum temperature": 'temperature.max',
    "Minimum temperature": 'temperature.min',
    "Total calorie": 'calorie.total',
    "Minimum heart rate": 'heart_rate.min',
    "Maximum heart rate": 'heart_rate.max'
}


dive_key_conversion = {
    "Dive": 'dive',
    "Total time": 'time.total',
    "Dive time": 'time.dive',
    "Surface time": 'time.surface',
    "Maximum depth": 'depth.max',
    "Maximum temperature": 'temperature.max',
    "Minimum temperature ": 'temperature.min',
    "Total calorie ": 'calorie.total',
    "Minimum heart rate": 'heart_rate.min',
    "Maximum heart rate": 'heart_rate.max',
    'data_points': 'data_points'
}

def pretty_temperature(dictionary, key, value):
    value, sign = value.split()

    if sign[-1:] == 'C':
        sign = 'celsius'
    else:
        sign = 'fahrenheit'
    put(dictionary, 'format.temperature', sign)

    return key, value


def pretty_distance(dictionary, key, value):
    value, sign = value.split()

    if sign[-1:] == 'm':
        sign = 'meter'
    else:
        sign = 'yard'
    put(dictionary, 'format.distance', sign)

    return key, value


def pretty_calorie(dictionary, key, value):
    value, sign = value.split()

    put(dictionary, 'format.calorie', sign)

    return key, value


class Omer(object):
    def __init__(self, file_name):
        self.file_name = file_name
        self.raw = {}
        self.summary = {}
        self.dives = {}
        self.read_file(file_name)

        self.parse_summary()
        self.pretty_summary()

        self.parse_dives()
        self.pretty_dives()

    def read_file(self, file_name):
        with codecs.open(file_name, 'r', encoding='utf16') as f:
            self.raw['content'] = f.readlines()

    def parse_summary(self):
        pattern = re.compile(ur'\"([^"]+?)\"', re.UNICODE)
        summary = {}

        for line in self.raw['content']:
            m = pattern.findall(line.strip())

            if m and len(m) == 2:
                key = m[0].encode('utf-8')
                value = m[1].encode('utf-8')

                if key == u'Dive':
                    break

                if value.isdigit():
                    summary[str(key)] = int(value)
                else:
                    summary[str(key)] = value

        self.raw['summary'] = summary

    def pretty_summary(self):
        summary = {}
        for k in self.raw['summary']:
            key = summary_key_conversion.get(k)
            if key:
                value = self.raw['summary'][k]
                if key.startswith('temperature'):
                    key, value = pretty_temperature(summary, key, value)
                elif key.startswith('depth'):
                    key, value = pretty_distance(summary, key, value)
                elif key.startswith('calorie'):
                    key, value = pretty_calorie(summary, key, value)

                put(summary, key, value)
            else:
                print "Warning: No key conversion for '%s'" % k

        self.summary = summary

    def parse_dives(self):
        pattern = re.compile(ur'\"([^"]+?)\"', re.UNICODE)
        raw_dives = []

        #print self.raw['content']
        dive_count = get(self.summary, 'dive.count')

        for number in range(1, dive_count + 1):
            start = self.raw['content'].index(u'"Dive"\t"{}"\n'.format(number))
            if number < dive_count:
                stop = self.raw['content'].index(u'"Dive"\t"{}"\n'.format(number + 1))
            else:
                stop = None

            raw_dives.append(self.raw['content'][start:stop])

        dives = []
        for raw_dive in raw_dives:
            dive = {}
            data_points = []
            for line in raw_dive:
                m = pattern.findall(line.strip())

                if m:
                    if len(m) == 2:
                        key = m[0].encode('utf-8')
                        value = m[1].encode('utf-8')

                        if value.isdigit():
                            dive[str(key)] = int(value)
                        else:
                            dive[str(key)] = value

                    if len(m) == 4:
                        item = m[0].encode('utf-8')
                        depth = m[1].encode('utf-8')
                        temp = m[2].encode('utf-8')
                        hr = m[3].encode('utf-8')

                        if item == u'Item':
                            continue

                        data_points.append({'item': item, 'depth': depth, 'temp': temp, 'hr': hr})

            dive['data_points'] = data_points
            dives.append(dive)

        self.raw['dives'] = dives

    def pretty_dives(self):
        dives = []
        for raw_dive in self.raw['dives']:
            dive = {}
            for k in raw_dive:
                key = dive_key_conversion.get(k)
                if key:
                    value = raw_dive[k]
                    if key.startswith('temperature'):
                        key, value = pretty_temperature(dive, key, value)
                    elif key.startswith('depth'):
                        key, value = pretty_distance(dive, key, value)
                    elif key.startswith('calorie'):
                        key, value = pretty_calorie(dive, key, value)

                    put(dive, key, value)
                else:
                    print "Warning: No key conversion for '%s'" % k

            dives.append(dive)

        self.dives = dives
