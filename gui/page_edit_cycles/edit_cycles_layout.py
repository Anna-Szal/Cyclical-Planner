import time
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty

from logic.input_preprocessing import *



class EditCyclesLayout(BoxLayout):
    cycles_list = ObjectProperty(None)
    info = ObjectProperty(None)
    input_task = ObjectProperty(None)
    input_period = ObjectProperty(None)
    input_date = ObjectProperty(None)

    def __init__(self, **kwargs):
        super(EditCyclesLayout, self).__init__(**kwargs)
        self.today = time.localtime()


    def on_parent(self, *largs):
        self.cycles_list.update()
        self.reset_new_cycle_fields()
        self.cycles_list.bind(alert=self.cycle_edit_error)


    def reset_new_cycle_fields(self):
        self.input_task.text = ''
        self.input_period.text = '1'
        self.input_date.text = f'{self.today[2]}.{self.today[1]}.{self.today[0]}'


    def create_new_cycle(self):
        new_cycle, message = preprocess_cycle(
            self.input_task.text,
            self.input_period.text,
            self.input_date.text
        )
        self.info.text = message
        if new_cycle is None:
            return

        print(new_cycle)
        App.get_running_app().db_logic.create_cycle(new_cycle)
        self.reset_new_cycle_fields()
        self.cycles_list.update()

    def cycle_edit_error(self, cycle_list, alert):
        self.info.text = alert