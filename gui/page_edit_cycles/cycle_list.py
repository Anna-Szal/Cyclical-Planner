from kivy.app import App
from kivy.factory import Factory

from gui.page_edit_cycles.cycle_row import CycleRow



class RemovePopup(Factory.Popup):
    def __init__(self, task, **kwargs):
        super(RemovePopup, self).__init__(**kwargs)
        self.task = task
        self.title=f'Removing cycle: "{task}"'
        self.size_hint = (None, None)
        self.size = (400, 400)


    def remove_cycle(self, **kwargs):
        App.get_running_app().db_logic.remove_cycle(self.task)
        self.dismiss()


    def remove_with_history(self, **kwargs):
        App.get_running_app().db_logic.remove_cycle(self.task)
        App.get_running_app().db_logic.remove_task_history(self.task)
        self.dismiss()



class CyclesList(Factory.ScrollView):
    alert = Factory.StringProperty('')
    cycle_list = Factory.ObjectProperty(None)

    def __init__(self, **kwargs):
        super(CyclesList, self).__init__(**kwargs)


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
        popup = RemovePopup(row.cycle.task)
        popup.bind(on_dismiss=self.popup_dismissed)
        popup.open()


    def popup_dismissed(self, popup):
        self.update()