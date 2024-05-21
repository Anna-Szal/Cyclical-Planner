from kivy.core.window import Window
from kivy.factory import Factory



class ButtonHLBg(Factory.Button):
    def __init__(self, highlight_color=(.9, .9, .9, 1), 
                 *args, **kwargs):
        super(ButtonHLBg, self).__init__(*args, **kwargs)
        self.original_color = self.background_color
        self.highlight_color = highlight_color
        Window.bind(mouse_pos=self.on_mouseover)


    def on_mouseover(self, inst, pos):
        if self.collide_point(*pos):
            self.background_color = self.highlight_color
        else:
            self.background_color = self.original_color



class ButtonHLText(Factory.Button):
    def __init__(self, highlight_color=(.9, .9, .9, 1), 
                 *args, **kwargs):
        super(ButtonHLText, self).__init__(*args, **kwargs)
        self.original_color = self.color
        self.highlight_color = highlight_color
        Window.bind(mouse_pos=self.on_mouseover)
        
    def on_mouseover(self, window, pos):
        if self.collide_point(*pos):
            self.color = self.highlight_color
        else:
            self.color = self.original_color



class ButtonOutline(Factory.Button):
    def __init__(self, outline_color=(.5, .5, .5, 1), *args, **kwargs):
        super(ButtonOutline, self).__init__(*args, **kwargs)
        self.outline = False

        with self.canvas.before:
            Factory.Color(*outline_color)
            self.line = Factory.Line(width=2)


    def on_size(self, instance, value):
        if self.outline:
            self.line.rectangle=([self.x, self.y, self.width, self.height])
