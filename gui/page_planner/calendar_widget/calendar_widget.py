import calendar
import time
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty, StringProperty



class CalendarWidget(Widget):
    m_title = StringProperty('')
    calendar_grid = ObjectProperty(None)

    def __init__(self, **kwargs):
        super(CalendarWidget, self).__init__(**kwargs)
        today = time.localtime()
        self.display_year = today[0]
        self.display_month = today[1]
        self.update()


    def update(self):
        month_name = str(calendar.month_name[self.display_month])
        self.m_title = f'{month_name} {self.display_year}'
        if self.calendar_grid is not None:
            self.calendar_grid.display_year = self.display_year
            self.calendar_grid.display_month = self.display_month
            self.calendar_grid.update()


    def next_month(self):
        if self.display_month == 12:
            self.display_month = 1
            self.display_year += 1
        else:
            self.display_month += 1
        self.update()


    def prev_month(self):
        if self.display_month == 1:
            self.display_month = 12
            self.display_year -= 1
        else:
            self.display_month -= 1
        self.update()
