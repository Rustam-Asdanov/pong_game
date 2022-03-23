import time
from turtle import Screen
from game_board import GameBoard, BOARD_HEIGHT, BOARD_WIDTH
from player import Player
from score_board import ScoreBoard
from ball import Ball

SCREEN_LEFT_END = -1 * BOARD_WIDTH / 2
SCREEN_RIGHT_END = BOARD_WIDTH / 2
SCREEN_TOP_END = BOARD_HEIGHT / 2
SCREEN_BOTTOM_END = -1 * BOARD_HEIGHT / 2

# Screen properties
screen = Screen()
screen.setup(width=BOARD_WIDTH, height=BOARD_HEIGHT)
screen.title("Pong game")
screen.bgcolor("black")
screen.listen()
screen.tracer(0)
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

ball = Ball()

while not game_over:
    screen.update()
    ball.move()
    time.sleep(0.01)

    if ball.xcor() > 380:
        score.add_score(1)
        score.update()
        ball.start_position()

    if ball.xcor() < -380:
        score.add_score(2)
        score.update()
        ball.start_position()

    if ball.ycor() > SCREEN_TOP_END - 20 or ball.ycor() < SCREEN_BOTTOM_END + 20:
        ball.bounce_y()

    if ball.distance(player_2) < 50 and ball.xcor() > SCREEN_RIGHT_END-30 or \
            ball.distance(player_1) < 50 and ball.xcor() < SCREEN_LEFT_END + 30:
        ball.bounce_x()

screen.exitonclick()
