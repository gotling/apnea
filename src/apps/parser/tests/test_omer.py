import inspect
import os
from django.test import TestCase
import time
from ..omer import Omer
from parser.dictionary import get


class TestOmer(TestCase):
    example_data = 'omer-up-x1-2015-01-31-eriksdalsbadet-25m.csv'

    def setUp(self):
        base_path = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe()))) + '/'
        test_file = os.path.join(base_path, 'data', self.example_data)
        #print test_file
        self.log = Omer(test_file)

    #def tearDown(self):
        # nothing

    def test_summary(self):
        log = self.log
        #print log.summary
        self.assertEqual(u'2015-01-30', log.raw['summary'][u'Date'])
        self.assertEqual(15, log.raw['summary'][u'No. of dives'])
        #self.assertEqual(time.strptime("01:17:59"), log.summary.time.total)

        self.assertEqual(u'01:17:59', get(log.summary, 'time.total'))
        self.assertEqual(u'00:01:26', get(log.summary, 'time.dive.average'))

        #print log.summary

        self.assertEqual(u'celsius', get(log.summary, 'format.temperature'))
        self.assertEqual(u'meter', get(log.summary, 'format.distance'))
        self.assertEqual(u'kCal', get(log.summary, 'format.calorie'))

    def test_dive(self):
        log = self.log

        self.assertTrue(log.raw['dives'])
        self.assertEqual(1, log.raw['dives'][0][u'Dive'])
        self.assertEqual("0.8", log.raw['dives'][0][u'data-points'][0]['depth'])
