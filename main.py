import time
from turtle import Screen
from game_board import GameBoard, BOARD_HEIGHT, BOARD_WIDTH
from player import Player
from score_board import ScoreBoard
from time import sleep

# Screen properties
screen = Screen()
screen.setup(width=BOARD_WIDTH, height=BOARD_HEIGHT)
screen.title("Pong game")
screen.bgcolor("black")
screen.listen()
game_over = False


def exit_game():
    user_choice = screen.textinput(title="Exit",
                                   prompt="Do you want to exit? (y/n)")

    if user_choice == "y":
        global game_over
        game_over = True
        screen.bye()


# Game board properties
board = GameBoard()
board.create()

# Score properties
score = ScoreBoard()

# Players properties
player_1 = Player("blue")
player_1.start_position("left")
screen.onkeypress(fun=player_1.move_up, key="w")
screen.onkeypress(fun=player_1.move_down, key="s")
player_2 = Player("green")
player_2.start_position("right")
screen.onkeypress(fun=player_2.move_up, key="Up")
screen.onkeypress(fun=player_2.move_down, key="Down")

screen.onkey(fun=exit_game, key="Escape")

while not game_over:
    screen.update()


screen.exitonclick()
