from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty



class StatisticsLayout(BoxLayout):
    year_grid = ObjectProperty()
    c_box = ObjectProperty()

    def __init__(self, **kwargs):
        super(StatisticsLayout, self).__init__(**kwargs)

    def on_parent(self, *largs):
        self.c_box.bind(selected_task=self.year_grid.mark_days)