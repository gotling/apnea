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
        self.content = {}
        self.raw = {}
        self.summary = {}
        self.read_file(file_name)
        self.parse_summary()
        self.pretty_summary()

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