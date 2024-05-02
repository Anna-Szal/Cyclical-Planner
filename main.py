from kivy.app import App
from gui.main_layout import MainLayout



class CyclicalPlannerApp(App):   
    def build(self):
        self.title = 'Cyclical Planner'

        return MainLayout()



if __name__ == '__main__':    
    app = CyclicalPlannerApp()    
    app.run()
