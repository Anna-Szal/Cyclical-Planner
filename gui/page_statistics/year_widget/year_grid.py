import time
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.properties import ObjectProperty, ListProperty

from logic.date import Date
from logic.calendar_logic import get_days_grid



class DayCell(Label):
    background_color = ListProperty((0, 0, 0, 0))
    def __init__(self, bg_color=(0, 0, 0, 0), *args, **kwargs):
        super(DayCell, self).__init__(*args, **kwargs)
        self.background_color = bg_color


class TodayCell(DayCell):
    pass


class YearGrid(GridLayout):
    chosen_date = ObjectProperty(None)

    def __init__(self, **kwargs):
        super(YearGrid, self).__init__(**kwargs)
        self.row_force_default = self.col_force_default = True
        self.row_default_height = self.col_default_width = 10

        self.today = time.localtime()
        self.today = Date(*self.today[:3])
        self.chosen_date = self.today
        self.display_year = self.today[0]
        self.update()


    def update(self):
        self.clear_widgets()
        
        days_grid = get_days_grid(self.display_year)
        for row in days_grid:
            for cell in row:
                display_month, display_day = cell
                if display_month == 0: 
                    bg_color = (0, 0, 0, 0)
                else:
                    bg_color = (.9,.9,.9, 1) if display_month % 2 == 0 else (.8,.8,.8, 1)

                if self.today ==  Date(self.display_year, display_month, display_day):
                    day_cell = TodayCell(bg_color)
                else:
                    day_cell = DayCell(bg_color)

                self.add_widget(day_cell)
                                        
