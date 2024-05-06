from kivy.app import App
from kivy.uix.stacklayout import StackLayout
from kivy.uix.scrollview import ScrollView
from kivy.properties import StringProperty

from gui.page_edit_cycles.cycle_row import CycleRow



class CyclesList(ScrollView):
    alert = StringProperty('')
    def __init__(self, **kwargs):
        super(CyclesList, self).__init__(**kwargs)

    def update(self):
        self.clear_widgets()
        cycles = App.get_running_app().logic.get_all_cycles()
        the_list = StackLayout()
        self.add_widget(the_list)
        for cycle in cycles:
            row = CycleRow(cycle)
            row.bind(alert=self.row_changed)
            the_list.add_widget(row)

    def row_changed(self, row, alert):
        self.alert = alert