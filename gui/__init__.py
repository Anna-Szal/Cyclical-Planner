import os
from kivy.lang import Builder

# imports needed in .kv files:
from .page_planner.planner_layout import PlannerLayout
from .page_planner.calendar_widget.calendar_widget import CalendarWidget
from .page_planner.calendar_widget.calendar_grid import CalendarGrid


script_path = os.path.realpath(__file__)
here = os.path.dirname(script_path)

Builder.load_file(os.path.join(here, 'theme.kv'))
Builder.load_file(os.path.join(here, 'main_layout.kv'))
Builder.load_file(os.path.join(here, 'page_planner', 'planner_layout.kv'))
Builder.load_file(os.path.join(here, 'page_planner', 'calendar_widget', 'calendar_widget.kv'))
Builder.load_file(os.path.join(here, 'page_planner', 'calendar_widget', 'calendar_grid.kv'))
