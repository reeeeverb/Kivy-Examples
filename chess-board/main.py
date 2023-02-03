import math
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import NumericProperty, ReferenceListProperty, ObjectProperty
from kivy.vector import Vector
from kivy.uix.image import Image
from kivy.core.window import Window
from kivy.graphics import Rectangle
from kivy.uix.button import Button
from kivy.lang.builder import Builder


class ChessGame(Widget):
    s_width = NumericProperty(Window.width)
    s_height = NumericProperty(Window.height)
    pass


class Chessboard(Widget):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.down_square = (0,0)
        self.names, self.color, self.piece = ["EMPTY"]*64, ["EMPTY"]*64, ["EMPTY"]*64
        p_size = NumericProperty()

    def on_touch_down(self, touch):
        if self.collide_point(*touch.pos):
            xpos = touch.pos[0]-self.pos[0]
            ypos = touch.pos[1]-self.pos[1]
            self.down_square = self.square_pos(xpos,ypos)
            self.reset_board()
            ## Testing

    def on_touch_up(self, touch):
        if self.collide_point(*touch.pos):
            xpos = touch.pos[0]-self.pos[0]
            ypos = touch.pos[1]-self.pos[1]
            up_square = self.square_pos(xpos,ypos)
            if up_square == self.down_square and up_square[2] != "EMPTY":
                self.show_moves(self.down_square)
            self.legal_move(self.down_square, up_square)

    def show_moves(self, square):
        c_size = 70
        forward = "WHITE"
        piece = self.piece[square[2]]
        color = self.color[square[2]]
        print(c_size)
        self.new_red = Image(source='chess-pieces/red-circle.png',size=(c_size,c_size))
        self.add_widget(self.new_red)
        if piece == "PAWN":
            if color == forward:
                if self.piece[square[2]+8] == "EMPTY":
                    self.parent.marker.markSpace(square[0]+1,square[1])
            else:
                if self.piece[square[2]-8] == "EMPTY":
                    self.parent.marker.markSpace(square[0]-1,square[1])

    def reset_board(self):
        self.parent.w_pawn0.set(1,0)
        self.parent.w_pawn0.makeVisible()
        self.parent.w_pawn1.set(1,1)
        self.parent.w_pawn1.makeVisible()
        self.parent.w_pawn2.set(1,2)
        self.parent.w_pawn2.makeVisible()
        self.parent.w_pawn3.set(1,3)
        self.parent.w_pawn3.makeVisible()
        self.parent.w_pawn4.set(1,4)
        self.parent.w_pawn4.makeVisible()
        self.parent.w_pawn5.set(1,5)
        self.parent.w_pawn5.makeVisible()
        self.parent.w_pawn6.set(1,6)
        self.parent.w_pawn6.makeVisible()
        self.parent.w_pawn7.set(1,7)
        self.parent.w_pawn7.makeVisible()

        self.parent.b_pawn0.set(6,0)
        self.parent.b_pawn0.makeVisible()
        self.parent.b_pawn1.set(6,1)
        self.parent.b_pawn1.makeVisible()
        self.parent.b_pawn2.set(6,2)
        self.parent.b_pawn2.makeVisible()
        self.parent.b_pawn3.set(6,3)
        self.parent.b_pawn3.makeVisible()
        self.parent.b_pawn4.set(6,4)
        self.parent.b_pawn4.makeVisible()
        self.parent.b_pawn5.set(6,5)
        self.parent.b_pawn5.makeVisible()
        self.parent.b_pawn6.set(6,6)
        self.parent.b_pawn6.makeVisible()
        self.parent.b_pawn7.set(6,7)
        self.parent.b_pawn7.makeVisible()

    def square_pos(self,x,y):
        square_size = self.width/8
        return (math.trunc(y/square_size),math.trunc(x/square_size),math.trunc(y/square_size)*8+math.trunc(x/square_size))

    def legal_move(self, down, up):
        if up[0] != 0:
            print(down, up)


class Pawn(Widget):
    position_row = NumericProperty(0)
    position_col = NumericProperty(0)
    white = NumericProperty(1)
    visible = NumericProperty(0)
    p_size = NumericProperty(0)

    def makeVisible(self):
        self.visible = 1
        self.parent.color[self.position_row*8+self.position_col] = "WHITE" if self.white == 1 else "BLACK"
    def makeNotVisible(self):
        self.visible = 0
        self.parent.color[self.position_row*8+self.position_col] = "EMPTY"
        self.parent.piece[row*8+col] = "PAWN"
    def set(self, row, col):
        self.position_col = col
        self.position_row = row
        if self.visible == 1:
            self.parent.color[row*8+col] = "WHITE" if self.white == 1 else "BLACK"
            self.parent.piece[row*8+col] = "PAWN"
    pass

class Marker(Widget):
    position_row = NumericProperty(0)
    position_col = NumericProperty(0)
    p_size = NumericProperty(0)
    visible = 1

    def markSpace(self, row, col):
        self.position_row = row
        self.position_col = col

class ChessApp(App):
    def build(self):
        return ChessGame()

if __name__ == '__main__':
    ChessApp().run()

