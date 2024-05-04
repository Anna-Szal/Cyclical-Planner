from kivy.uix.gridlayout import GridLayout
from kivy.properties import ObjectProperty
import gui.building_blocks as bb



class ArrowButton(bb.ButtonHLText):
    pass


class PlannerLayout(GridLayout):
    done_list = ObjectProperty(None)    
    todo_list = ObjectProperty(None)
    done_calendar = ObjectProperty(None)
    todo_calendar = ObjectProperty(None)

    # called when a widget instance is added/removed from a parent
    def on_parent(self, *largs):
        # disabling future/past buttons
        self.done_calendar.calendar_grid.no_future = True
        self.done_calendar.calendar_grid.update() 

        self.todo_calendar.calendar_grid.no_past = True
        self.todo_calendar.calendar_grid.update()

        dummy_list = ['jogging', 'study', 'hairdresser']
        self.todo_list.update(dummy_list)