from turtle import Turtle
import constants as c


class Ball(Turtle):
    def __init__(self):
        # Init turtle
        super().__init__(shape='circle')
        self.color(c.BALL_COLOR)
        self.shapesize(c.BALL_SIZE, c.BALL_SIZE)
        self.speed('fastest')
        self.penup()
