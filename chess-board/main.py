from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import NumericProperty, ReferenceListProperty
from kivy.vector import Vector
from kivy.uix.image import Image

class ChessGame(Widget):
    pass

class ChessApp(App):
    def build(self):
        return ChessGame()

class Chessboard(Widget):
    wimg = Image(source='board.png')

if __name__ == '__main__':
    ChessApp().run()

