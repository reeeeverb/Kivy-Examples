from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import NumericProperty, ReferenceListProperty
from kivy.vector import Vector
from kivy.uix.image import Image
from kivy.core.window import Window

class ChessGame(Widget):
    s_width = NumericProperty(Window.width)
    s_height = NumericProperty(Window.height)
    pass

class Chessboard(Widget):
    def on_touch_down(self, touch):
        if self.collide_point(*touch.pos):
            print(touch.pos)

class ChessApp(App):
    def build(self):
        return ChessGame()

#class Chessboard(Widget):
    #wimg = Image(source='board.png')

if __name__ == '__main__':
    ChessApp().run()

