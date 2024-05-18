import os
from kivy.lang import Builder

# imports needed in .kv files:
from .page_planner.planner_layout import PlannerLayout
from .page_planner.task_list import TaskList
from .page_planner.calendar_widget.calendar_widget import CalendarWidget
from .page_planner.calendar_widget.calendar_grid import CalendarGrid

from .page_edit_cycles.edit_cycles_layout import EditCyclesLayout
from .page_edit_cycles.cycle_list import CyclesList
from .page_edit_cycles.cycle_row import CycleRow
from .page_edit_cycles.new_cycle import NewCycle

from .page_statistics.statistics_layout import StatisticsLayout, ComboBox
from .page_statistics.year_widget.year_grid import YearGrid, DayCell



script_path = os.path.realpath(__file__)
here = os.path.dirname(script_path)

Builder.load_file(os.path.join(here, 'theme.kv'))
Builder.load_file(os.path.join(here, 'main_layout.kv'))
Builder.load_file(os.path.join(here, 'page_planner', 'planner_layout.kv'))
Builder.load_file(os.path.join(here, 'page_planner', 'task_list.kv'))
Builder.load_file(os.path.join(here, 'page_planner', 'calendar_widget', 'calendar_widget.kv'))
Builder.load_file(os.path.join(here, 'page_planner', 'calendar_widget', 'calendar_grid.kv'))

Builder.load_file(os.path.join(here, 'page_edit_cycles', 'edit_cycles_layout.kv'))
Builder.load_file(os.path.join(here, 'page_edit_cycles', 'cycle_list.kv'))
Builder.load_file(os.path.join(here, 'page_edit_cycles', 'cycle_row.kv'))
Builder.load_file(os.path.join(here, 'page_edit_cycles', 'new_cycle.kv'))

Builder.load_file(os.path.join(here, 'page_statistics', 'statistics_layout.kv'))
Builder.load_file(os.path.join(here, 'page_statistics', 'year_widget', 'year_grid.kv'))
