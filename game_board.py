from turtle import Turtle

BOARD_WIDTH = 800
BOARD_HEIGHT = 600


class GameBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white","blue")
        self.width = 20
        # self.hideturtle()
        self.penup()
        self.setposition(0, y=-1 * BOARD_HEIGHT / 2)
        self.setheading(90)
        self.pensize(10)


    def create(self):
        while self.ycor() < BOARD_HEIGHT/2:
            self.forward(20)
            self.pendown()
            self.forward(20)
            self.penup()
