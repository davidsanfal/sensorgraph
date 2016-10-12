import datetime
from django import forms
from sensors.utils.sensor_utils import sensor_types
from sensors.models import Sensor


def sensor_options():
     sensors = set(Sensor.objects.values_list('sensor', flat=True))
     return tuple([(s, s) for s in sensors])

class GraphForm(forms.Form):
    init=forms.DateField(initial=datetime.date.today)
    end=forms.DateField(initial=datetime.date.today)

    SIGNALS = tuple([(k, k) for k in sensor_types.keys()])
    SENSORS = sensor_options()
    PERIOD = (('day', 'day'),
              ('week', 'week'),
              ('month', 'month'))
    sensor = forms.ChoiceField(choices=SENSORS, required=True, label="Sensor")
    signal = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple,
                                       choices=SIGNALS,
                                       required=True,
                                       label="Signals")
    period = forms.ChoiceField(choices=PERIOD, required=True, label="Period")
