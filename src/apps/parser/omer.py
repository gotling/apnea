# coding: utf-8
import json
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


def pretty_temperature(key, value, dictionary=False):
    value, sign = value.split()

    if dictionary:
        if sign[-1:] == 'C':
            sign = 'celsius'
        else:
            sign = 'fahrenheit'

        put(dictionary, 'format.temperature', sign)

    return key, float(value)


def pretty_distance(key, value, dictionary=False):
    value, sign = value.split()

    if dictionary:
        if sign[-1:] == 'm':
            sign = 'meter'
        else:
            sign = 'yard'
        put(dictionary, 'format.distance', sign)

    return key, float(value)


def pretty_calorie(key, value, dictionary=False):
    value, sign = value.split()

    if dictionary:
        put(dictionary, 'format.calorie', sign)

    return key, float(value)



class Omer(object):
    def __init__(self, file_name):
        self.file_name = file_name
        self.raw = {}
        self.summary = {}
        self.dives = {}
        self.content = {}

        self.read_file(file_name)

        self.parse_summary()
        self.pretty_summary()

        self.parse_dives()
        self.pretty_dives()

    def read_file(self, file_name):
        with codecs.open(file_name, 'r', encoding='utf16') as f:
            self.raw['content'] = f.readlines()

    def export(self, file_name):
        with open(file_name, 'w') as outfile:
            json.dump(self.content, outfile, sort_keys=False, indent=4)

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
                    key, value = pretty_temperature(key, value, dictionary=summary)
                elif key.startswith('depth'):
                    key, value = pretty_distance(key, value, dictionary=summary)
                elif key.startswith('calorie'):
                    key, value = pretty_calorie(key, value, dictionary=summary)

                put(summary, key, value)
            else:
                print "Warning: No key conversion for '%s'" % k

        self.summary = summary
        self.content['summary'] = summary

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
            dive = {'summary': {}}
            data_points = []
            for line in raw_dive:
                m = pattern.findall(line.strip())

                if m:
                    if len(m) == 2:
                        key = m[0].encode('utf-8')
                        value = m[1].encode('utf-8')

                        if value.isdigit():
                            dive['summary'][str(key)] = int(value)
                        else:
                            dive['summary'][str(key)] = value

                    if len(m) == 4:
                        item = m[0].encode('utf-8')
                        depth = m[1].encode('utf-8')
                        temp = m[2].encode('utf-8')
                        hr = m[3].encode('utf-8')

                        if item == u'Item':
                            continue

                        data_points.append({'item': int(item), 'depth': float(depth), 'temp': float(temp), 'hr': int(hr)})

            dive['data_points'] = data_points
            dives.append(dive)

        self.raw['dives'] = dives

    def pretty_dives(self):
        dives = []
        for raw_dive in self.raw['dives']:
            summary = {}
            for k in raw_dive['summary']:
                key = dive_key_conversion.get(k)
                if key:
                    value = raw_dive['summary'][k]
                    if key.startswith('temperature'):
                        key, value = pretty_temperature(key, value)
                    elif key.startswith('depth'):
                        key, value = pretty_distance(key, value)
                    elif key.startswith('calorie'):
                        key, value = pretty_calorie(key, value)

                    put(summary, key, value)
                else:
                    print "Warning: No key conversion for '%s'" % k

            dives.append({'summary': summary, 'data_points': raw_dive['data_points']})

        self.dives = dives
        self.content['dives'] = dives
