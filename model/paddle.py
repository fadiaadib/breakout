from turtle import Turtle
import constants as c


class Paddle(Turtle):
    def __init__(self):
        super().__init__(shape='square')
        self.color(c.PADDLE_COLOR)
        self.shapesize(0.5, c.PADDLE_WIDTH)
        self.penup()
        self.goto(0, 30 - c.SCREEN_HEIGHT / 2)
        self.speed('fastest')

    def move_right(self):
        if (self.xcor() + 50) < (c.SCREEN_WIDTH / 2):
            self.forward(c.PADDLE_SPEED)

    def move_left(self):
        if (self.xcor() - 50) > (-c.SCREEN_WIDTH / 2):
            self.backward(c.PADDLE_SPEED)
