from typing import Dict
import datetime
from datetime import date, time

class Weather:
    """Attributes of the weather on todays date"""
    _todays_date: datetime.date
    _temps: Dict[str, int]
    _feels_like: Dict[str, int]
    _pop: float
    _sunset: datetime.time

    def __init__(self, data: list):
        """Create Weather object on today's date and process cleaned weather data

        Precondition: data is in the order:
            [TEMPERATURES, FEELS LIKE, PROBABILITY OF PRECIP, SUNSET TIME]
        """
        self._todays_date = date.today()
        self._temps = data[0]
        self._feels_like = data[1]
        self._pop = data[2]
        self._sunset = datetime.datetime.fromtimestamp(data[3]).time()

    def get_date(self):
        return '{} {}, {}'.format(self._todays_date.strftime('%B'),
                                  self._todays_date.day,
                                  self._todays_date.year)

    def get_morning_temp(self):
        return round(self._temps['morn'] - 273.15)

    def get_afternoon_temp(self):
        return round(self._temps['day'] - 273.15)

    def get_evening_temp(self):
        return round(self._temps['eve'] - 273.15)

    def get_night_temp(self):
        return round(self._temps['night'] - 273.15)

    def get_feels_like_day(self):
        return round(self._feels_like['day'] - 273.15)

    def get_feels_like_eve(self):
        return round(self._feels_like['eve'] - 273.15)

    def get_feels_like_night(self):
        return round(self._feels_like['night'] - 273.15)

    def get_pop(self):
        return '{}%'.format(self._pop*100)

    def get_sunset_time(self):
        if self._sunset.hour < 12:
            ampm = 'am'
        else:
            ampm = 'pm'
        return '{} {}'.format(datetime.time(self._sunset.hour%12, self._sunset.minute,
                             self._sunset.second), ampm)

    def __str__(self):
        return "Weather forecast on {}:\n\nProbability of Precipitation: {}\n" \
               "Time of Sunset: {}\n\nMorning: {}   Feels Like: n/a\n\n" \
               "Afternoon: {}   Feels Like: {}\n\nEvening: {}   Feels Like: {}\n\n" \
               "Night: {}   Feels Like: {}".format(self.get_date(), self.get_pop(),
                                                   self.get_sunset_time(), self.get_morning_temp(),
                                                   self.get_afternoon_temp(), self.get_feels_like_day(),
                                                   self.get_evening_temp(), self.get_feels_like_eve(),
                                                   self.get_night_temp(), self.get_feels_like_night())
