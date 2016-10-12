import datetime
from django.db import models

class Sensor(models.Model):
	sensor = models.CharField(max_length=30)
	acquisition_date = models.DateField()
	signal = models.CharField(max_length=60)
	timestamp = models.DateTimeField()
	value = models.FloatField()
