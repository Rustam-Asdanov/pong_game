from turtle import Screen
from game_board import GameBoard
from player import Player
from score_board import ScoreBoard

screen = Screen()
screen.setup(width=600, height=400)
screen.bgcolor("black")

board = GameBoard()

screen.exitonclick()
