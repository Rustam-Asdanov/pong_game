from turtle import Turtle
from game_board import BOARD_HEIGHT, BOARD_WIDTH


class Player(Turtle):

    def __init__(self, color):
        super().__init__()
        self.color(color)
        self.shapesize(stretch_wid=3, stretch_len=0.7)
        self.shape("square")
        self.penup()

    def start_position(self, position):
        if position == "left":
            self.setposition(-1 * BOARD_WIDTH / 2 + 20, 0)
        if position == "right":
            self.setposition(BOARD_WIDTH / 2 - 20, 0)
