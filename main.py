from turtle import Screen
from game_board import GameBoard, BOARD_HEIGHT, BOARD_WIDTH
from player import Player
from score_board import ScoreBoard

screen = Screen()
screen.setup(width=BOARD_WIDTH, height=BOARD_HEIGHT)
screen.title("Pong game")
screen.bgcolor("black")

board = GameBoard()
board.create()

screen.exitonclick()
