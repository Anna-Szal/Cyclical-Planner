from kivy.app import App
from kivy.factory import Factory

from logic.cycle import Cycle
from logic.input_preprocessing import *



class CycleRow(Factory.BoxLayout):
    alert = Factory.StringProperty('')
    removed = Factory.BooleanProperty(False)

    def __init__(self, cycle: Cycle, **kwargs):
        super(CycleRow, self).__init__(**kwargs)
        self.cycle = cycle

        self.db_logic = App.get_running_app().db_logic

        self.task_input = Factory.TextInput(text=cycle.task, multiline=False)
        self.task_input.bind(on_text_validate=self.edit_task)
        self.add_widget(self.task_input)

        self.period_input = Factory.TextInput(text=str(cycle.period), multiline=False)
        self.period_input.bind(on_text_validate=self.edit_period)
        self.add_widget(self.period_input)

        self.date_input = Factory.TextInput(text=cycle.next_date.f_string(), multiline=False)
        self.date_input.bind(on_text_validate=self.edit_date)
        self.add_widget(self.date_input)

        self.remove_btn = Factory.Button(
            text='-', size_hint_x=None, width=30, font_size=40)
        self.remove_btn.bind(on_press=self.remove_cycle)
        self.add_widget(self.remove_btn)   


    def edit_task(self, task_input):
        old_task_name = self.cycle.task
        new_task_name, msg = preprocess_task(task_input.text)
        if new_task_name:
            self.cycle.task = new_task_name
            self.db_logic.update_cycle(old_task_name, self.cycle)
            self.db_logic.update_task(old_task_name, new_task_name)
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


    def remove_cycle(self, *args):
        self.removed = True
        