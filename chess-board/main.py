import math
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
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.down_square = (0,0)

    def on_touch_down(self, touch):
        if self.collide_point(*touch.pos):
            xpos = touch.pos[0]-self.pos[0]
            ypos = touch.pos[1]-self.pos[1]
            self.down_square = self.square_pos(xpos,ypos)

    def on_touch_up(self, touch):
        if self.collide_point(*touch.pos):
            xpos = touch.pos[0]-self.pos[0]
            ypos = touch.pos[1]-self.pos[1]
            up_square = self.square_pos(xpos,ypos)
            self.legal_move(self.down_square, up_square)

    def square_pos(self,x,y):
        square_size = self.width/8
        return (math.trunc(y/square_size)+1,math.trunc(x/square_size)+1)

    def legal_move(self, down, up):
        if up[0] != 0:
            print(down, up)

class ChessApp(App):
    def build(self):
        return ChessGame()

if __name__ == '__main__':
    ChessApp().run()

