from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.properties import ListProperty, ObjectProperty
from kivy.core.window import Window



class ArrowButton(Button):
    original_color = ListProperty([0, 0, 0, 1])
    highlight_color = ListProperty([.9, .9, .9, 1])

    def __init__(self, *args, **kwargs):
        super(ArrowButton, self).__init__(*args, **kwargs)
        self.color = self.original_color
        Window.bind(mouse_pos=self.on_mouseover)
        
    def on_mouseover(self, window, pos):
        if self.collide_point(*pos):
            self.color = self.highlight_color
        else:
            self.color = self.original_color


class PlannerLayout(GridLayout):
    done_calendar = ObjectProperty(None)
    todo_calendar = ObjectProperty(None)

    # called when a widget instance is added/removed from a parent
    def on_parent(self, *largs):
        # disabling future/past buttons
        self.done_calendar.calendar_grid.no_future = True
        self.done_calendar.calendar_grid.update() 

        self.todo_calendar.calendar_grid.no_past = True
        self.todo_calendar.calendar_grid.update()