from kivy.app import App
from kivy.graphics import Color, Rectangle
from kivy.uix.widget import Widget


class DrawingWidget(Widget):
    def __init__(self):
        super(DrawingWidget, self).__init__()

        with self.canvas:
            Color(1, 1, 1, 1)  # rouge, vert, bleu, alpha
            self.rect = Rectangle(size=self.size,
                                  pos=self.pos)
        self.bind(pos=self.update_rectangle,
                  size=self.update_rectangle)

    def update_rectangle(self, instance, value):
        self.rect.pos = self.pos
        self.rect.size = self.size


class DrawingApp(App):
    def build(self):
        root_widget = DrawingWidget()
        return root_widget


DrawingApp().run()
