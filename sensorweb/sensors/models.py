import datetime
from django.db import models


class Sensor(models.Model):
	'''
	sensor: sensor name.
	acquisition_date: CSV date.
	signal: thermometer, anemometer, hygrometer,
	        barometer, radiometer, pluviometer.
	timestamp: read timestamp.
	value: measure value.
	'''
	sensor = models.CharField(max_length=30)
	acquisition_date = models.DateField()
	signal = models.CharField(max_length=60)
	timestamp = models.DateTimeField()
	value = models.FloatField()
