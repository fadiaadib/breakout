from turtle import Turtle
import constants as c
import random


class Ball(Turtle):
    def __init__(self):
        # Init turtle
        super().__init__(shape='circle')
        self.color(c.BALL_COLOR)
        self.shapesize(c.BALL_SIZE, c.BALL_SIZE)
        self.speed('fastest')
        self.penup()
        self.velocity = c.BALL_SPEED
        self.restart()
        self.radius = c.BALL_SIZE*c.CONV/2

    def move(self):
        self.forward(self.velocity)

    def restart(self):
        self.goto(x=0, y=0)
        self.velocity = c.BALL_SPEED
        self.setheading(random.randint(*c.BALL_ORIENT))

    def bounce(self, side):
        if side == 'h':
            self.setheading(360 - self.heading())
        else:
            self.setheading(180 - self.heading())

    def bounds(self):
        # Returns tuple (w,n,e,s)
        return (self.xcor() - self.radius,
                self.ycor() + self.radius,
                self.xcor() + self.radius,
                self.ycor() - self.radius)
