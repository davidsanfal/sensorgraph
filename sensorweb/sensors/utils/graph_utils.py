import datetime
import time
from dateutil.relativedelta import relativedelta
from graphos.sources.simple import SimpleDataSource
from graphos.renderers.flot import LineChart
from sensors.models import Sensor
from sensors.utils.sensor_utils import sensor_types


period_delta = {'day': datetime.timedelta(days=1),
                'week': datetime.timedelta(days=7),
                'month': relativedelta(months=1)}


def graphs(query):
    '''Return a graph list ready to be drawn with a sensor/signal info'''
    retrieved = []
    for signal in query['signal']:
        rows = Sensor.objects.filter(signal=signal,
                                     sensor=query['sensor'],
                                     acquisition_date__range=(query['init'],
                                                              query['end']))
        title = "%s-%s" %(signal, query['sensor'])
        data = [[query['period'], title]]
        dataset = split_dataset(rows,
                                signal,
                                query['init'],
                                query['end'],
                                query['period'])
        print(dataset)
        if dataset:
            data.extend(dataset)
            options = {'title': title,
                       'xaxis': {'mode': 'time',
                                 'timezone': 'browser',
                                 'axisLabel': 'Date Time',
                                 'minTickSize': [1, "day"],
                                 'timeformat': r"%y/%m/%d"},
                       'series': {'lines': {'show': True},
                                  'points': {'show': True,
                                             'dataLabels': True}},
                        'grid': {'hoverable': True, 'clickable': False }
                        }
            retrieved.append((signal,
                              LineChart(SimpleDataSource(data=data),
                                                         options=options)))
    print('retrieved', retrieved)
    return retrieved


def split_dataset(rows, signal, init, end, period):
    '''Split and group a row list in periods [days/weeks/months]
       Return a graph dataset'''
    step = init + period_delta[period]
    step = step if step < end else end
    dataset = []
    in_period = True
    while in_period and rows:
        in_period = step < end
        step = step if in_period else end
        group = []
        for row in rows:
            if init <= row.acquisition_date < step:
                group.append(row)
        if group:
            measure = sensor_types[signal]['grouping']([r.value for r in group])
            dataset.append([int(time.mktime(init.timetuple())) * 1000, measure])
            rows = list(set(rows).difference(group))
        init = step
        step = init + period_delta[period]
    return dataset
