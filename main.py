import os
from kivy.app import App

from gui.main_layout import MainLayout
from persistence.setup import create_tables



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
    app.run()
