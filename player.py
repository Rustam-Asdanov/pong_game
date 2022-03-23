from turtle import Turtle
from game_board import BOARD_HEIGHT, BOARD_WIDTH


class Player(Turtle):

    def __init__(self, color):
        super().__init__()
        self.color(color)
        self.shapesize(stretch_wid=0.7, stretch_len=3)
        self.setheading(90)
        self.shape("square")
        self.penup()

    def start_position(self, position):
        if position == "left":
            self.setposition(-1 * BOARD_WIDTH / 2 + 20, 0)
        if position == "right":
            self.setposition(BOARD_WIDTH / 2 - 20, 0)

    def move_up(self):
        if self.ycor() < BOARD_HEIGHT / 2 - 40:
            self.forward(15)

    def move_down(self):
        if self.ycor() > -1 * BOARD_HEIGHT / 2 + 40:
            self.backward(15)
