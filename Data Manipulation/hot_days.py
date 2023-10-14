"""
Write a function get_hot_work_days() that creates a new list hot_work_days
from the list weekday_temperatures.
Only days that are not weekends and had temperatures greater than
or equal to 30 degrees Celcius should be included in this new list.
The entries in the new list are to be represented as tuples (date, temperature).

Result:
[('2019-07-15', 31), ('2019-07-16', 33), ('2019-07-19', 30), ('2019-07-23', 31)]

"""

weekday_temperatures = [
    {'day': 'Monday', 'date': '2019-07-15', 'temperature': 31},
    {'day': 'Tuesday', 'date': '2019-07-16', 'temperature': 33},
    {'day': 'Wednesday', 'date': '2019-07-17', 'temperature': 27},
    {'day': 'Thursday', 'date': '2019-07-18', 'temperature': 25},
    {'day': 'Friday', 'date': '2019-07-19', 'temperature': 30},
    {'day': 'Saturday', 'date': '2019-07-20', 'temperature': 31},
    {'day': 'Sunday', 'date': '2019-07-21', 'temperature': 29},
    {'day': 'Monday', 'date': '2019-07-22', 'temperature': 25},
    {'day': 'Tuesday', 'date': '2019-07-23', 'temperature': 31},
    {'day': 'Wednesday', 'date': '2019-07-24', 'temperature': 26},
    {'day': 'Thursday', 'date': '2019-07-25', 'temperature': 23},
    {'day': 'Friday', 'date': '2019-07-26', 'temperature': 22},
    {'day': 'Saturday', 'date': '2019-07-27', 'temperature': 23},
    {'day': 'Sunday', 'date': '2019-07-28', 'temperature': 32}
]


def get_hot_work_days(lst):
    hot_work_days = []
    for dic in lst:
        if dic['day'] != 'Saturday' and dic['day'] != 'Sunday': 
            if dic['temperature'] >= 30:
                hot_work_days.append( ( dic["date"], dic["temperature"] ) )
    return hot_work_days


def lcomp_get_hot_work_days(lst):
    return [
        (dic["date"], dic["temperature"]) for dic in lst if
        dic['day']!= 'Saturday' and dic['day'] != 'Sunday' and dic['temperature'] >= 30
           ]


print(get_hot_work_days(weekday_temperatures))

print(lcomp_get_hot_work_days(weekday_temperatures))