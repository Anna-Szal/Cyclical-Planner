from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.properties import ObjectProperty, StringProperty



class ComboBox(TextInput):
    container = ObjectProperty()

    def __init__(self, **kwargs):
        super(ComboBox, self).__init__(**kwargs)
        self.multiline=False
        self.db_logic = App.get_running_app().db_logic


    def on_text(self, instance, value):
        self.container.clear_widgets()
            
        if value != '':
            tasks = sorted(self.db_logic.get_tasks_start_with(value))

            for word in tasks:
                btn = Button(text=word, on_press=self.select_word, size_hint_y=None, height=50)
                self.container.add_widget(btn)


    def select_word(self, btn):
        self.text = btn.text
        self.on_text_validate()


    def on_text_validate(self, **kwargs):
        print(self.text)            



class StatisticsLayout(BoxLayout):
    m_title = StringProperty('')
    year_grid = ObjectProperty(None)

    def __init__(self, **kwargs):
        super(StatisticsLayout, self).__init__(**kwargs)
