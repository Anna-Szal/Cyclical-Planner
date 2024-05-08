from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import StringProperty, ObjectProperty, BooleanProperty

from logic.input_preprocessing import *



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


    def reset_new_cycle_fields(self):
        self.input_task.text = ''
        self.input_period.text = '1'
        self.input_date.text = f'{self.today[2]}.{self.today[1]}.{self.today[0]}'
        self.created = False


    def create_new_cycle(self):
        print('new from NewCycle')
        new_cycle, message = preprocess_cycle(
            self.input_task.text,
            self.input_period.text,
            self.input_date.text
        )
        self.alert = message
        if new_cycle is None:
            return

        App.get_running_app().db_logic.create_cycle(new_cycle)
        self.created = True
        
