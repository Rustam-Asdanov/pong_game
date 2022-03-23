from turtle import Turtle
from game_board import BOARD_WIDTH, BOARD_HEIGHT


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.x_move = 5
        self.y_move = 5
        self.start_position()

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def start_position(self):
        self.hideturtle()
        self.goto(0, 0)
        self.showturtle()
        self.bounce_x()

    def bounce_y(self):
        self.y_move *= -1

    def bounce_x(self):
        self.x_move *= -1
