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
        self.wall_collisions = 0
        self.top_collision = False
        self.brick_collision = False
        self.turn = 1

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
        time.sleep(c.REFRESH_PERIOD)

    def reset_collisions(self):
        self.wall_collisions = 0
        self.top_collision = False
        self.brick_collision = False

    def increment_turn(self):
        self.turn += 1
        if self.turn > c.ROUNDS:
            self.ball.delete()
            self.score.game_over(win=True)
            self.screen.update()
            return False
        else:
            self.score.update_round(self.turn)
            self.ball.restart()
            self.wall.restart()
            self.paddle.restart()
            self.screen.update()
            time.sleep(c.RESTART_PERIOD)
            return True

    def play(self):
        while True:
            self.update()
            self.ball.move()

            # Check collision with paddle:
            self.paddle.check_collision(self.ball)

            # Check collision with bricks wall
            points, speedup = self.wall.check_collision(self.ball)
            if points:
                self.score.update_score(points)
                self.wall_collisions += 1
                if not self.wall.bricks and not self.increment_turn():
                    break
                if self.wall_collisions % 4 == 0 or self.wall_collisions % 12 == 0:
                    self.ball.speedup()
                if speedup and not self.brick_collision:
                    self.brick_collision = True
                    self.ball.speedup()

            # Check collision with board walls or life
            board_collision = self.board.check_collision(self.ball)
            if board_collision == 'bottom':
                self.reset_collisions()
                self.score.update_lives(-1)
                if self.score.out_of_lives():
                    self.score.game_over(win=False)
                    break
                else:
                    self.ball.restart()
                    self.screen.update()
                    time.sleep(c.RESTART_PERIOD)
            elif board_collision == 'top' and not self.top_collision:
                self.top_collision = True
                self.ball.speedup()
                self.paddle.shrink()


if __name__ == '__main__':
    Breakout()
