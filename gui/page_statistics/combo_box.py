from kivy.app import App
from kivy.factory import Factory



class ComboBox(Factory.TextInput):
    container = Factory.ObjectProperty()
    selected_task = Factory.StringProperty()

    def __init__(self, **kwargs):
        super(ComboBox, self).__init__(**kwargs)
        self.multiline=False
        self.db_logic = App.get_running_app().db_logic
        

    def on_double_tap(self, **kwargs):
        if self.text == '':
            self.update_dropdown('')


    def update_dropdown(self, string):
        self.container.clear_widgets()
        self.container.height = 0

        tasks = sorted(self.db_logic.get_tasks_start_with(string))

        for word in tasks:
            btn = Factory.Button(
                text=word, on_press=self.select_word, size_hint_y=None, height=50)
            
            self.container.add_widget(btn)  
            self.container.height += btn.height


    def on_text(self, instance, value):
        self.update_dropdown(value)


    def select_word(self, btn):
        self.text = btn.text
        self.on_text_validate()


    def on_text_validate(self, **kwargs):
        self.selected_task = self.text            
