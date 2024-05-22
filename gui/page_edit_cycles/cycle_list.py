from kivy.app import App
from kivy.factory import Factory

from gui.page_edit_cycles.cycle_row import CycleRow



class RemovePopup(Factory.BoxLayout):
    def __init__(self, **kwargs):
        super(RemovePopup, self).__init__(**kwargs)



class CyclesList(Factory.ScrollView):
    alert = Factory.StringProperty('')
    cycle_list = Factory.ObjectProperty(None)

    def __init__(self, **kwargs):
        super(CyclesList, self).__init__(**kwargs)
        self.popup = Factory.Popup(
            content=RemovePopup(), 
            size_hint = (None, None),
            size = (400, 400)
            )


    def update(self):
        self.cycle_list.clear_widgets()
        self.cycle_list.height = 0
        cycles = App.get_running_app().db_logic.get_all_cycles()
        for cycle in cycles:
            row = CycleRow(cycle)
            row.bind(alert=self.row_changed)
            row.bind(removed=self.cycle_removed)
            self.cycle_list.add_widget(row)
            self.cycle_list.height += row.height


    def row_changed(self, row, alert):
        self.alert = alert


    def cycle_removed(self, row, removed):
        self.popup.title=f'Removing cycle: "{row.cycle.task}"'
        self.popup.open()