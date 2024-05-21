from kivy.factory import Factory



class StatisticsLayout(Factory.BoxLayout):
    year_grid = Factory.ObjectProperty()
    c_box = Factory.ObjectProperty()

    def __init__(self, **kwargs):
        super(StatisticsLayout, self).__init__(**kwargs)

    def on_parent(self, *largs):
        self.c_box.bind(selected_task=self.year_grid.mark_days)