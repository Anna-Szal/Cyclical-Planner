from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty, StringProperty



class StatisticsLayout(BoxLayout):
    m_title = StringProperty('')
    year_grid = ObjectProperty(None)

    def __init__(self, **kwargs):
        super(StatisticsLayout, self).__init__(**kwargs)
