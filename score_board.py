from turtle import Turtle
from game_board import BOARD_HEIGHT, BOARD_WIDTH


class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.player_one_score = 0
        self.player_two_score = 0
        self.penup()
        self.color("red")
        self.hideturtle()
        self.speed("fastest")
        self.setposition(x=0, y=BOARD_HEIGHT / 2 - 60)
        self.update()

    def update(self):
        self.write(arg=f"{self.player_one_score} : {self.player_two_score}",
                   align="center", font=("Arial", 40, "bold"))

    def add_score(self, player_id):
        if player_id == 1:
            self.player_one_score += 1

        if player_id == 2:
            self.player_two_score += 1