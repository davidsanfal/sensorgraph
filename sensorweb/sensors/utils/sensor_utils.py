def average(data):
    return sum(data) / float(len(data))

sensor_types = {'thermometer': {'grouping': average},
                'anemometer': {'grouping': average},
                'hygrometer': {'grouping': average},
                'barometer': {'grouping': average},
                'radiometer': {'grouping': average},
                'pluviometer': {'grouping': sum}}
