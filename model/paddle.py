from turtle import Turtle

import constants as c
from helpers import *
from model.ball import Ball


class Paddle(Turtle):
    def __init__(self):
        super().__init__(shape='square')
        self.color(c.PADDLE_COLOR)
        self.shapesize(c.PADDLE_HEIGHT/c.CONV, c.PADDLE_WIDTH/c.CONV)
        self.penup()
        self.goto(0, c.PADDLE_SOUTH_GAP - c.SCREEN_HEIGHT / 2)
        self.speed('fastest')
        self.sound = 'paddle'

    def bounds(self):
        return (self.xcor() - c.PADDLE_WIDTH / 2,
                self.ycor() + c.PADDLE_HEIGHT / 2,
                self.xcor() + c.PADDLE_WIDTH / 2,
                self.ycor() - c.PADDLE_HEIGHT / 2)

    def move_right(self):
        if (self.xcor() + c.PADDLE_WIDTH/2) < (c.SCREEN_WIDTH / 2):
            self.forward(c.PADDLE_SPEED)

    def move_left(self):
        if (self.xcor() - c.PADDLE_WIDTH/2) > (-c.SCREEN_WIDTH / 2):
            self.backward(c.PADDLE_SPEED)

    def check_collision(self, ball: Ball):
        bw, bn, be, bs = ball.bounds()
        bx, by = ball.pos()
        w, n, e, s = self.bounds()

        if (n >= by >= s) and (is_close(be, w) or is_close(bw, e)):
            ball.bounce('v')
            audio.play(self.sound)

        elif (w <= bx <= e) and (is_close(bn, s) or is_close(bs, n)):
            ball.bounce('h')
            audio.play(self.sound)
