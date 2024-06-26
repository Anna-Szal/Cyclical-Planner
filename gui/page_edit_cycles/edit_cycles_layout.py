from kivy.factory import Factory

from logic.input_preprocessing import *



class EditCyclesLayout(Factory.BoxLayout):
    cycles_list = Factory.ObjectProperty(None)
    info = Factory.ObjectProperty(None)
    new_cycle = Factory.ObjectProperty(None)

    def __init__(self, **kwargs):
        super(EditCyclesLayout, self).__init__(**kwargs)


    def on_parent(self, *largs):
        self.cycles_list.update()
        self.cycles_list.bind(alert=self.cycle_edit_error)

        self.new_cycle.reset_new_cycle_fields()   
        self.new_cycle.bind(alert=self.cycle_edit_error)
        self.new_cycle.bind(created=self.created_new_cycle)


    def created_new_cycle(self, *largs):
        if self.new_cycle.created == True:
            self.new_cycle.reset_new_cycle_fields()
            self.cycles_list.update()


    def cycle_edit_error(self, cycle_list, alert):
        self.info.text = alert
