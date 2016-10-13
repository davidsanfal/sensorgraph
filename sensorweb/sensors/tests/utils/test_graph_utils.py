from datetime import datetime
from django.test import TestCase
from sensors.utils.graph_utils import split_dataset
from sensors.exceptions import FileContentException
from sensors.models import Sensor


class GraphUtilsTestCase(TestCase):

    def setUp(self):
        Sensor(sensor='sensor',
               acquisition_date=datetime.strptime('01012000',"%d%m%Y").date(),
               signal='thermometer',
               timestamp=datetime.fromtimestamp(946681200),
               value=12).save()
        Sensor(sensor='sensor',
               acquisition_date=datetime.strptime('01012000',"%d%m%Y").date(),
               signal='thermometer',
               timestamp=datetime.fromtimestamp(946681201),
               value=14).save()
        Sensor(sensor='sensor',
               acquisition_date=datetime.strptime('02012000',"%d%m%Y").date(),
               signal='thermometer',
               timestamp=datetime.fromtimestamp(946767600),
               value=4.5).save()

    def test_split_dataset_day(self):
        result = split_dataset(Sensor.objects.all(),
                               'thermometer',
                               datetime.strptime('30121999',"%d%m%Y").date(),
                               datetime.strptime('03012000',"%d%m%Y").date(),
                               'day')
        self.assertEqual([[946684800000, 13.0], [946771200000, 4.5]], result)

    def test_split_dataset_week(self):
        result = split_dataset(Sensor.objects.all(),
                               'thermometer',
                               datetime.strptime('30121999',"%d%m%Y").date(),
                               datetime.strptime('03012000',"%d%m%Y").date(),
                               'week')
        self.assertEqual([[946512000000, 10.166666666666666]], result)

    def test_split_dataset_month(self):
        result = split_dataset(Sensor.objects.all(),
                               'thermometer',
                               datetime.strptime('30121999',"%d%m%Y").date(),
                               datetime.strptime('03012000',"%d%m%Y").date(),
                               'month')
        self.assertEqual([[946512000000, 10.166666666666666]], result)
