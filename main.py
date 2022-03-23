from turtle import Screen
from game_board import GameBoard, BOARD_HEIGHT, BOARD_WIDTH
from player import Player
from score_board import ScoreBoard

# Screen properties
screen = Screen()
screen.setup(width=BOARD_WIDTH, height=BOARD_HEIGHT)
screen.title("Pong game")
screen.bgcolor("black")

# Game board properties
board = GameBoard()
board.create()

# Score properties
score = ScoreBoard()

# Players properties
player_1 = Player("blue")
player_1.start_position("left")
player_2 = Player("green")
player_2.start_position("right")

screen.exitonclick()
