from turtle import Screen

from model.ball import Ball
from model.game_board import GameBoard
from model.paddle import Paddle
from model.scoreboard import Scoreboard
import constants as c


class App:
    def __init__(self):
        self.screen = Screen()
        self.screen.tracer(0)
        self.screen.setup(width=c.SCREEN_W, height=c.SCREEN_H)
        self.screen.bgcolor(c.BG_COLOR)
        self.screen.title(c.TITLE)

        self.ball = Ball()
        self.paddle = Paddle()
        self.scoreboard = Scoreboard()
        self.board = GameBoard()

        self.create_bindings()

    def create_bindings(self):
        # Create listeners
        self.screen.listen()


if __name__ == '__main__':
    app = App()
    app.screen.exitonclick()
