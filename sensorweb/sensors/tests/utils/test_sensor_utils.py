from django.test import TestCase
from sensors.utils.sensor_utils import average

class SensorUtilsTestCase(TestCase):

    def test_average(self):
        self.assertEqual(average([2,3]), 2.5)
