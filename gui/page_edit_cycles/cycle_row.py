from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.properties import StringProperty

from logic.cycle import Cycle
from logic.input_preprocessing import *



class CycleRow(BoxLayout):
    alert = StringProperty('')

    def __init__(self, cycle: Cycle, **kwargs):
        super(CycleRow, self).__init__(**kwargs)
        self.cycle = cycle

        self.db_logic = App.get_running_app().db_logic

        self.task_input = TextInput(text=cycle.task, multiline=False)
        self.task_input.bind(on_text_validate=self.edit_task)
        self.add_widget(self.task_input)

        self.period_input = TextInput(text=str(cycle.period), multiline=False)
        self.period_input.bind(on_text_validate=self.edit_period)
        self.add_widget(self.period_input)

        self.date_input = TextInput(text=cycle.next_date.f_string(), multiline=False)
        self.date_input.bind(on_text_validate=self.edit_date)
        self.add_widget(self.date_input)        


    def edit_task(self, task_input):
        task, msg = preprocess_task(task_input.text)
        if task:
            old_task_name = self.cycle.task
            self.cycle.task = task
            self.db_logic.update_cycle(old_task_name, self.cycle)
        else:
           self.alert = msg
           self.task_input.text = self.cycle.task


    def edit_period(self, period_input):
        period, msg = preprocess_period(period_input.text)
        if period:
            self.cycle.period = period
            self.db_logic.update_cycle(self.cycle.task, self.cycle)
        else:
            self.alert = msg
            self.period_input.text = str(self.cycle.period)


    def edit_date(self, date_input):
        date, msg = preprocess_next_date(date_input.text)
        if date:
            self.cycle.next_date = date
            self.db_logic.update_cycle(self.cycle.task, self.cycle)
        else:
            self.alert = msg
            self.date_input.text = self.cycle.next_date.f_string()