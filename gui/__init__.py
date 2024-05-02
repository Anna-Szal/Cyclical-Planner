import os
from kivy.lang import Builder

# imports needed in .kv files:
from .page_planner.planner_layout import PlannerLayout



script_path = os.path.realpath(__file__)
here = os.path.dirname(script_path)

Builder.load_file(os.path.join(here, 'theme.kv'))
Builder.load_file(os.path.join(here, 'main_layout.kv'))
Builder.load_file(os.path.join(here, 'page_planner', 'planner_layout.kv'))
