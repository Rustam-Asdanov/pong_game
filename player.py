from turtle import Turtle
from game_board import BOARD_HEIGHT, BOARD_WIDTH


class Player(Turtle):

    def __init__(self, color):
        super().__init__()
        self.hideturtle()
        self.shape("square")
        self.penup()
        self.color(color)
        self.shapesize(stretch_wid=3, stretch_len=0.7)
        self.showturtle()

    def start_position(self, position):
        if position == "left":
            self.setposition(-1 * BOARD_WIDTH / 2 + 20, 0)
        if position == "right":
            self.setposition(BOARD_WIDTH / 2 - 20, 0)

    def move_up(self):
        if self.ycor() <= 260:
            self.goto(y=self.ycor() + 10, x=self.xcor())

    def move_down(self):
        if self.ycor() >= -260:
            self.goto(y=self.ycor() - 10, x=self.xcor())
