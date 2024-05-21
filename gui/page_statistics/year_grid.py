import time
from kivy.app import App
from kivy.factory import Factory
import kivy.utils

from logic.date import Date
from logic.calendar_logic import get_days_grid



class DayCell(Factory.Label):
    background_color = Factory.ListProperty((0, 0, 0, 0))
    def __init__(self, bg_color=(0, 0, 0, 0), *args, **kwargs):
        super(DayCell, self).__init__(*args, **kwargs)
        self.background_color = bg_color


class TodayCell(DayCell):
    pass


class YearGrid(Factory.GridLayout):
    chosen_date = Factory.ObjectProperty(None)

    def __init__(self, **kwargs):
        super(YearGrid, self).__init__(**kwargs)
        self.db_logic = App.get_running_app().db_logic
        self.marked_days = set()

        self.spacing = [2, 2]

        self.row_force_default = self.col_force_default = True
        self.row_default_height = self.col_default_width = 10

        self.width = 0
        self.height = self.row_default_height*7 + self.spacing[1]*6
        self.today = time.localtime()
        self.today = Date(*self.today[:3])
        self.chosen_date = self.today
        self.display_year = self.today[0]
        self.update()


    def update(self):
        self.clear_widgets()
        
        days_grid = get_days_grid(self.display_year)
        days_in_row = len(days_grid[0])
        self.width = days_in_row*self.col_default_width + self.spacing[0]*(days_in_row-1)
        for row in days_grid:
            for cell in row:
                display_month, display_day = cell
                display_date = Date(self.display_year, display_month, display_day)
                if display_date in self.marked_days:
                    bg_color = kivy.utils.get_color_from_hex('#A9E1D0') 
                elif display_month == 0: 
                    bg_color = (0, 0, 0, 0)
                else:
                    bg_color = (.9,.9,.9, 1) if display_month % 2 == 0 else (.8,.8,.8, 1)

                if self.today == display_date:
                    day_cell = TodayCell(bg_color)
                else:
                    day_cell = DayCell(bg_color)

                self.add_widget(day_cell)


    def mark_days(self, instance, value):
        dates = self.db_logic.get_done_dates(value)
        self.marked_days = set(dates)
        self.update()
