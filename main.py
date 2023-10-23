from turtle import Screen
from tkinter import TclError
import time

from model.ball import Ball
from model.wall import Wall
from model.board import Board
from model.paddle import Paddle
from model.scoreboard import Scoreboard
import constants as c


class Breakout:
    def __init__(self):
        self.screen = Screen()
        self.screen.tracer(0)
        self.screen.setup(width=c.SCREEN_WIDTH, height=c.SCREEN_HEIGHT)
        self.screen.bgcolor(c.BG_COLOR)
        self.screen.title(c.TITLE)

        self.paddle = Paddle()
        self.wall = Wall()
        self.score = Scoreboard()
        self.board = Board()
        self.ball = Ball()

        self.key_bindings()
        self.play()
        try:
            self.screen.exitonclick()
        except TclError:
            pass

    def key_bindings(self):
        # Create listeners
        self.screen.listen()
        self.screen.onkey(self.paddle.move_right, 'Right')
        self.screen.onkey(self.paddle.move_left, 'Left')

    def update(self):
        self.screen.update()
        time.sleep(0.005)

    def play(self):
        try:
            while True:
                self.update()
                self.ball.move()

                # Check collision with paddle:
                self.paddle.check_collision(self.ball)

                # Check collision with bricks wall
                points = self.wall.check_collision(self.ball)
                if points:
                    self.score.update_score(points)

                # Check collision with board walls or fail
                if not self.board.check_collision(self.ball):
                    self.score.update_lives(-1)
                    if self.score.game_over():
                        break
                    else:
                        time.sleep(0.6)
                        self.ball.restart()
        except TclError:
            pass


if __name__ == '__main__':
    game = Breakout()
