from kivy.uix.tabbedpanel import TabbedPanel




class MainLayout(TabbedPanel):
    def __init__(self, **kwargs):
        super(MainLayout, self).__init__(**kwargs)
        self._tab_layout.padding = '0dp', '0dp', '0dp', '-2dp'