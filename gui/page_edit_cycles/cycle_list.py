from kivy.app import App
from kivy.uix.scrollview import ScrollView
from kivy.properties import StringProperty, ObjectProperty

from gui.page_edit_cycles.cycle_row import CycleRow



class CyclesList(ScrollView):
    alert = StringProperty('')
    cycle_list = ObjectProperty(None)

    def __init__(self, **kwargs):
        super(CyclesList, self).__init__(**kwargs)

    def update(self):
        self.cycle_list.clear_widgets()
        self.cycle_list.height = 0
        cycles = App.get_running_app().db_logic.get_all_cycles()
        for cycle in cycles:
            row = CycleRow(cycle)
            row.bind(alert=self.row_changed)
            self.cycle_list.add_widget(row)
            self.cycle_list.height += row.height

    def row_changed(self, row, alert):
        self.alert = alert