from turtle import Screen
import time
from model.ball import Ball
from model.wall import Wall
from model.game_board import GameBoard
from model.paddle import Paddle
from model.scoreboard import Scoreboard
import constants as c


class App:
    def __init__(self):
        self.screen = Screen()
        self.screen.tracer(0)
        self.screen.setup(width=c.SCREEN_WIDTH, height=c.SCREEN_HEIGHT)
        self.screen.bgcolor(c.BG_COLOR)
        self.screen.title(c.TITLE)

        self.ball = Ball()
        self.paddle = Paddle()
        self.wall = Wall()
        self.scoreboard = Scoreboard()
        self.board = GameBoard()

        self.create_bindings()
        self.start()

    def create_bindings(self):
        # Create listeners
        self.screen.listen()
        self.screen.onkey(self.paddle.move_right, 'Right')
        self.screen.onkey(self.paddle.move_left, 'Left')

    def start(self):
        while True:
            self.screen.update()
            time.sleep(0.05)


if __name__ == '__main__':
    app = App()
    app.screen.exitonclick()
