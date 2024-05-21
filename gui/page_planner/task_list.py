from kivy.factory import Factory



class TaskButton(Factory.ToggleButton):
    pass


class TaskList(Factory.ScrollView):
    task_list = Factory.ObjectProperty(None)

    def __init__(self, **kwargs):
        super(TaskList, self).__init__(**kwargs)
        self.chosen_task = ''

    def update(self, plans):
        self.task_list.clear_widgets()
        self.task_list.height = 0
        self.chosen_task = ''
        for plan in plans:
            tb = TaskButton(text=plan, group='plan')
            tb.bind(state=self.toggle)
            self.task_list.add_widget(tb)
            self.task_list.height += tb.height
            
    def toggle(self, tb, state):
        if state == 'down':
            self.chosen_task = tb.text
            tb.color = (1, 1, 1, 1)
        else:
            tb.color = (0, 0, 0, 1)
