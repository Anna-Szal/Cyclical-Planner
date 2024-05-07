import os
from kivy.app import App

from logic.db_logic import DbLogic
from gui.main_layout import MainLayout
from persistence.setup import create_tables
from persistence.db_todo import DbTodo
from persistence.db_done import DbDone



class CyclicalPlannerApp(App):   
    def build(self):
        self.title = 'Cyclical Planner'
        return MainLayout()



if __name__ == '__main__':
    script_path = os.path.realpath(__file__)
    here = os.path.dirname(script_path)
    db_path = os.path.join(here, 'persistence', 'database.db')
    if not os.path.exists(db_path):
        create_tables(db_path)

    app = CyclicalPlannerApp()
    app.db_logic = DbLogic(DbTodo(db_path), DbDone(db_path))
    app.run()
