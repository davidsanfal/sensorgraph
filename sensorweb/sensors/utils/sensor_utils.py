'''
    Dictionary with the relation between sensor type
    and the function to calculate the aggregate measure.
    TODO: Moves the sensor_types to a config file or a DB.
'''

def average(data):
    return sum(data) / float(len(data))

sensor_types = {'thermometer': {'grouping': average},
                'anemometer': {'grouping': average},
                'hygrometer': {'grouping': average},
                'barometer': {'grouping': average},
                'radiometer': {'grouping': average},
                'pluviometer': {'grouping': sum}}
