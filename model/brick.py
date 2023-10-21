from turtle import Turtle
import constants as c


class Brick(Turtle):
    def __init__(self):
        super().__init__(shape='square')
        self.shapesize(0.5, c.BRICK_WIDTH/c.CONV)
        self.penup()
        self.score = 0


class YellowBrick(Brick):
    def __init__(self):
        super().__init__()
        self.color('yellow')
        self.score = 1


class GreenBrick(Brick):
    def __init__(self):
        super().__init__()
        self.color('green')
        self.score = 3


class OrangeBrick(Brick):
    def __init__(self):
        super().__init__()
        self.color('orange')
        self.score = 5


class RedBrick(Brick):
    def __init__(self):
        super().__init__()
        self.color('red')
        self.score = 7
