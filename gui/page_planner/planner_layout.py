from kivy.app import App
from kivy.factory import Factory

import gui.building_blocks as bb



class ArrowButton(bb.ButtonHLText):
    pass


class PlannerLayout(Factory.GridLayout):
    done_list = Factory.ObjectProperty(None)    
    todo_list = Factory.ObjectProperty(None)
    done_calendar = Factory.ObjectProperty(None)
    todo_calendar = Factory.ObjectProperty(None)

    def __init__(self, **kwargs):
        super(PlannerLayout, self).__init__(**kwargs)         
        self.db_logic = App.get_running_app().db_logic
        self.db_logic.shift_dates_on_startup()

    # called when a widget instance is added/removed from a parent
    def on_parent(self, *largs):
        self.chosen_done_date = self.done_calendar.calendar_grid.chosen_date
        self.chosen_todo_date = self.todo_calendar.calendar_grid.chosen_date
        self.done_calendar.calendar_grid.bind(chosen_date=self.on_done_date_change)
        self.todo_calendar.calendar_grid.bind(chosen_date=self.on_todo_date_change)

        # disabling future/past buttons
        self.done_calendar.calendar_grid.no_future = True
        self.done_calendar.calendar_grid.update() 

        self.todo_calendar.calendar_grid.no_past = True
        self.todo_calendar.calendar_grid.update()

        self.update_done_list()
        self.update_todo_list()


    def on_done_date_change(self, grid_obj, date):
        self.chosen_done_date = date
        self.update_done_list()


    def on_todo_date_change(self, grid_obj, date):
        self.chosen_todo_date = date
        self.update_todo_list()


    def update_done_list(self):
        tasks = self.db_logic.get_done_tasks(self.chosen_done_date)
        self.done_list.update(tasks)        


    def update_todo_list(self):
        tasks = self.db_logic.get_todo_tasks(self.chosen_todo_date)
        self.todo_list.update(tasks)      


    def move_to_done(self):
        if self.todo_list.chosen_task != '':

            self.db_logic.move_to_done(
                self.todo_list.chosen_task, 
                self.chosen_done_date
                )

            self.update_done_list()
            self.update_todo_list()
            self.todo_list.chosen_task = ''
