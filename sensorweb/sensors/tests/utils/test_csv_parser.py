from datetime import datetime
from django.test import TestCase
from sensors.utils.csv_parser import parse_line, save_sensor
from sensors.exceptions import FileContentException
from sensors.models import Sensor


class CSVParserTestCase(TestCase):

    def test_parse_line(self):
        result = parse_line('sensor', '17111988', b'thermometer,946681205,12.49')
        expected = Sensor(sensor='sensor',
                          acquisition_date=datetime.strptime('17111988',
                                                             "%d%m%Y").date(),
                          signal='thermometer',
                          timestamp=datetime.fromtimestamp(946681205),
                          value=12.49)

        self.assertEqual(result.sensor, expected.sensor)
        self.assertEqual(result.acquisition_date, expected.acquisition_date)
        self.assertEqual(result.timestamp, expected.timestamp)
        self.assertEqual(result.value, expected.value)
        self.assertEqual(result.signal, expected.signal)

    def test_parse_error(self):
        self.assertRaises(FileContentException, parse_line, 'sensor',
                                                            '17111988',
                                                            't,946681205,1')
        self.assertRaises(FileContentException, parse_line, 'sensor',
                                                            '17111988',
                                                            b't-946681205-1')
        self.assertRaises(FileContentException, parse_line, 'sensor',
                                                            '17111988',
                                                            b'')

    def test_save_sensor(self):
        result = Sensor(sensor='sensor',
                        acquisition_date=datetime.strptime('17111988',
                                                           "%d%m%Y").date(),
                        signal='thermometer',
                        timestamp=datetime.fromtimestamp(946681205),
                        value=12.49)
        save_sensor(result)
        expected = Sensor.objects.get(sensor='sensor')
        self.assertEqual(result.sensor, expected.sensor)
        self.assertEqual(result.acquisition_date, expected.acquisition_date)
        self.assertEqual(result.value, expected.value)
        self.assertEqual(result.signal, expected.signal)


    def test_save_sensor_error(self):
        result = 'sensor_fake'
        self.assertRaises(FileContentException, save_sensor, result)
