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
        self.collisions = 0
        self.top_collision = False

        self.key_bindings()
        try:
            self.play()
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
        time.sleep(0.001)

    def play(self):
        while True:
            self.update()
            self.ball.move()

            # Check collision with paddle:
            self.paddle.check_collision(self.ball)

            # Check collision with bricks wall
            points = self.wall.check_collision(self.ball)
            if points:
                self.score.update_score(points)
                self.collisions += 1
                if self.collisions % 4 == 0 or self.collisions % 12 == 0:
                    self.ball.speedup()

            # Check collision with board walls or fail
            board_collision = self.board.check_collision(self.ball)
            if board_collision == 'bottom':
                self.collisions = 0
                self.top_collision = False
                self.score.update_lives(-1)
                if self.score.game_over():
                    break
                else:
                    time.sleep(0.6)
                    self.ball.restart()
            elif board_collision == 'top' and not self.top_collision:
                self.top_collision = True
                self.ball.speedup()


if __name__ == '__main__':
    game = Breakout()
