from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import StringProperty, ObjectProperty, BooleanProperty

from logic.input_preprocessing import *
from logic.date import Date



class NewCycle(BoxLayout):
    alert = StringProperty('')
    created = BooleanProperty(False)
    input_task = ObjectProperty(None)
    input_period = ObjectProperty(None)
    input_date = ObjectProperty(None)

    def __init__(self, **kwargs):
        super(NewCycle, self).__init__(**kwargs)
        self.db_logic = App.get_running_app().db_logic
        self.today = time.localtime()
        self.today = Date(*self.today[:3])


    def reset_new_cycle_fields(self):
        self.input_task.text = ''
        self.input_period.text = '1'
        self.input_date.text = self.today.f_string()
        self.created = False


    def create_new_cycle(self):
        new_cycle, message = preprocess_cycle(
            self.input_task.text,
            self.input_period.text,
            self.input_date.text
        )
        self.alert = message
        if new_cycle is None:
            return

        returned = self.db_logic.get_cycle(new_cycle.task)
        if not returned:
            self.db_logic.create_cycle(new_cycle)
            self.created = True
        else:
            self.alert = 'cycle with this task name already exists'
        
