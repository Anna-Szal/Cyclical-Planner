import calendar
import time
import datetime
from kivy.factory import Factory

import gui.building_blocks as bb
from logic.date import Date


class CalendarButton(bb.ButtonHLBg, bb.ButtonOutline):
    pass

class ChosenButton(bb.ButtonOutline):
    pass


class CalendarGrid(Factory.GridLayout):
    chosen_date = Factory.ObjectProperty(None)
    no_future = Factory.BooleanProperty(False)
    no_past = Factory.BooleanProperty(False)

    def __init__(self, **kwargs):
        super(CalendarGrid, self).__init__(**kwargs)
        today = time.localtime()
        self.today_date = Date(*today[:3])
        self.chosen_date = self.today_date
        self.display_year = today[0]
        self.display_month = today[1]

        self.update()


    def update(self):
        self.clear_widgets()
        
        weeks = calendar.monthcalendar(self.display_year, self.display_month)
        for week in weeks:
            for display_day in week:
                if display_day == 0: 
                    day_btn = Factory.Label(text='')
                    self.add_widget(day_btn)
                    continue
                
                display_date = Date(self.display_year, self.display_month, display_day)

                if self.chosen_date == display_date:
                    day_btn = ChosenButton()              
                else:
                    day_btn = CalendarButton()
                    weekday = calendar.weekday(*display_date) 
                    if weekday > 4:
                        day_btn.color = (.40, .78, .74, 1)    

                if self.today_date == display_date:
                    day_btn.outline = True

                day_btn.text = str(display_day)
                day_btn.bind(on_press=self.callback)
                
                if self.no_future:
                    d0 = datetime.date(*display_date)
                    d1 = datetime.date(*self.today_date)
                    if d0 > d1:
                        day_btn.disabled = True

                if self.no_past:
                    d0 = datetime.date(*display_date)
                    d1 = datetime.date(*self.today_date)
                    if d0 < d1:
                        day_btn.disabled = True

                self.add_widget(day_btn)


    def callback(self, day_btn):
        self.chosen_date = Date(
            self.display_year, 
            self.display_month, 
            int(day_btn.text)
            )
        self.update()
