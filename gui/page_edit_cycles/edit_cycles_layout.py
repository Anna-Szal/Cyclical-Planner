import time
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.stacklayout import StackLayout
from kivy.uix.textinput import TextInput
from kivy.properties import ObjectProperty
from kivy.uix.scrollview import ScrollView

from logic.cycle import Cycle
from logic.date import Date



class CycleRow(BoxLayout):           
    def __init__(self, cycle: Cycle, **kwargs):
        super(CycleRow, self).__init__(**kwargs)
        self.cycle = cycle
        date_str = f'{cycle.next_date.day}.{cycle.next_date.month}.{cycle.next_date.year}'

        task_ti = TextInput(text=cycle.task, multiline=False)
        task_ti.bind(on_text_validate=self.edit_task)
        self.add_widget(task_ti)

        period_ti = TextInput(text=str(cycle.period), multiline=False)
        period_ti.bind(on_text_validate=self.edit_period)
        self.add_widget(period_ti)

        date_ti = TextInput(text=date_str, multiline=False)
        date_ti.bind(on_text_validate=self.edit_date)
        self.add_widget(date_ti)        


    def edit_task(self, task_ti):
        self.cycle.task = task_ti.text
        print(self.cycle.task)


    def edit_period(self, period_ti):
        self.cycle.period = int(period_ti.text)
        print(self.cycle.period)


    def edit_date(self, date_ti):
        date = self.parent.parent.process_date(date_ti.text)
        if date:
            self.cycle.next_date = date
            App.get_running_app().logic.update_cycle(self.cycle.task, self.cycle)


class CyclesList(ScrollView):
    def __init__(self, **kwargs):
        super(CyclesList, self).__init__(**kwargs)

    def update(self):
        self.clear_widgets()
        cycles = App.get_running_app().logic.get_all_cycles()
        the_list = StackLayout()
        self.add_widget(the_list)
        for cycle in cycles:
            the_list.add_widget(CycleRow(cycle))


class EditCyclesLayout(BoxLayout):
    cycles_list = ObjectProperty(None)
    info = ObjectProperty(None)
    input_task = ObjectProperty(None)
    input_period = ObjectProperty(None)
    input_date = ObjectProperty(None)

    def __init__(self, **kwargs):
        super(EditCyclesLayout, self).__init__(**kwargs)
    

    def on_parent(self, *largs):
        self.cycles_list.update()
        self.reset_new_cycle_fields()


    def reset_new_cycle_fields(self):
        self.input_task.text = ''
        self.input_period.text = '1'
        today = time.localtime()
        self.input_date.text = f'{today[2]}.{today[1]}.{today[0]}'


    def create_new_cycle(self):
        task = self.input_task.text
        period = self.input_period.text
        next_date = self.input_date.text

        if task == '' or period == '' or next_date =='':
            self.info.text = 'all the fields are required'
            return

        period = self.process_period(period)
        if not period: return
        
        next_date = self.process_date(next_date)
        if not next_date: return

        today = time.localtime()
        if next_date.delta_with(today[:3]) < 0:
            self.info.text = "make sure next date of the cycle is not in the past"
            return

        self.info.text = ''
        App.get_running_app().logic.create_cycle(Cycle(task, period, next_date))
        self.reset_new_cycle_fields()
        self.cycles_list.update()


    def process_date(self, date):
        try:
            date = date.split('.')
            date = Date(int(date[2]), int(date[1]), int(date[0]))
        except:
            self.info.text = 'dates should have format DD.MM.YYYY'
            return None

        return date
    

    def process_period(self, period):
        try:
            period = int(period)
        except ValueError as e:
            self.info.text = 'period should be a number (days), no additional symbols allowed'
            return None
        
        return period