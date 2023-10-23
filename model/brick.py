from turtle import Turtle

import constants as c
from helpers import *
from model.ball import Ball


class Brick(Turtle):
    def __init__(self):
        super().__init__(shape='square')
        self.shapesize(c.BRICK_HEIGHT / c.CONV, c.BRICK_WIDTH / c.CONV)
        self.penup()
        self.points = 0
        self.alive = True
        self.sound = 'brick'
        self.speedup = False

    def check_collision(self, ball: Ball):
        if self.alive:
            bw, bn, be, bs = ball.bounds()
            bx, by = ball.pos()
            w, n, e, s = self.bounds()

            if (n >= by >= s) and (is_close(be, w) or is_close(bw, e)):
                ball.bounce('v')
                self.color(c.BRICK_DEAD_COLOR)
                self.alive = False
                audio.play(self.sound)

            elif (w <= bx <= e) and (is_close(bn, s) or is_close(bs, n)):
                ball.bounce('h')
                self.color(c.BRICK_DEAD_COLOR)
                self.alive = False
                audio.play(self.sound)

            return not self.alive
        return False

    def bounds(self):
        return (self.xcor() - c.BRICK_WIDTH / 2,
                self.ycor() + c.BRICK_HEIGHT / 2,
                self.xcor() + c.BRICK_WIDTH / 2,
                self.ycor() - c.BRICK_HEIGHT / 2)


class YellowBrick(Brick):
    def __init__(self):
        super().__init__()
        self.color('yellow')
        self.points = 1


class GreenBrick(Brick):
    def __init__(self):
        super().__init__()
        self.color('green')
        self.points = 3


class OrangeBrick(Brick):
    def __init__(self):
        super().__init__()
        self.color('orange')
        self.points = 5
        self.speedup = True


class RedBrick(Brick):
    def __init__(self):
        super().__init__()
        self.color('red')
        self.points = 7
        self.speedup = True
