from kivy.uix.stacklayout import StackLayout
from kivy.uix.togglebutton import ToggleButton




class TaskButton(ToggleButton):
    pass


class TaskList(StackLayout):

    def __init__(self, **kwargs):
        super(TaskList, self).__init__(**kwargs)
        self.chosen_plan = ''


    def update(self, plans):
        self.clear_widgets()
        self.chosen_plan = ''
        for plan in plans:
            tb = TaskButton(text=plan, group='plan')
            tb.bind(state=self.toggle)
            self.add_widget(tb)
            

    def toggle(self, tb, state):
        if state == 'down':
            self.chosen_plan = tb.text
            tb.color = (1, 1, 1, 1)
        else:
            tb.color = (0, 0, 0, 1)