from typing import NamedTuple
import datetime
import time



class Date(NamedTuple):
    year: int
    month: int
    day: int

    def delta_with(self, date):
        d0 = datetime.date(*self)
        d1 = datetime.date(*date)
        delta = d0 - d1
        return int(delta.days)
    
    def get_shifted_date(self, days: int):
        d0 = datetime.date(*self)
        d0 = d0 + datetime.timedelta(days=days)
        return Date(d0.year, d0.month, d0.day)
    
    def f_string(self):

        return datetime.date(*self).strftime('%d.%m.%Y')