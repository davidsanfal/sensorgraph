import os
import datetime
from collections import defaultdict
from sensors.models import Sensor
from sensors.exceptions import FileContentException, FileNameException


def parser(files):
    '''Parse a file list and converts each line in a Sensor'''
    if files:
        file_names = []
        for csv in files:
            file_names.append(csv._name)
            try:
                sensor, acquisition_date = csv._name.replace('.csv', '').split('-')
            except:
                raise FileNameException("Invalid Name: %s" % csv._name)
            for n, line in enumerate(csv.read().splitlines()):
                try:
                    save_sensor(parse_line(sensor, acquisition_date, line))
                except FileContentException:
                    msg = "Invalid Content in %s:\nLine %i - %s" % (csv._name, n+1, line)
                    raise FileContentException(msg)
        return file_names

def parse_line(sensor, acquisition_date, line):
    '''Parse and converts a line in a Sensor'''
    try:
        signal, timestamp, value = line.decode().split(',')
        return Sensor(sensor=sensor,
                      acquisition_date=datetime.datetime.strptime(acquisition_date, "%d%m%Y").date(),
                      signal=signal,
                      timestamp=datetime.datetime.fromtimestamp(int(timestamp)),
                      value=float(value))
    except:
        raise FileContentException()


def save_sensor(sensor):
    '''Save a Sensor in the DB'''
    try:
        rows = Sensor.objects.filter(sensor=sensor.sensor,
                                     signal=sensor.signal,
                                     timestamp=sensor.timestamp)
        if rows:
            for row in rows:
                if (row.acquisition_date < sensor.acquisition_date):
                    row.sensor=sensor
                    row.acquisition_date=sensor.acquisition_date
                    row.signal=sensor.signal
                    row.timestamp=sensor.timestamp
                    row.value=sensor.value
                    row.save()
        else:
            sensor.save()
    except:
        raise FileContentException()
