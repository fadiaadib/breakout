from turtle import Turtle
import constants as c


class Scoreboard(Turtle):
    def __init__(self):
        # Init turtle
        super().__init__(visible=False)
        self.penup()
        self.color(c.FONT_COLOR)

        self.score = 0
        self.lives = c.LIVES
        self.show()

    def show(self):
        self.clear()
        self.goto(x=60-c.SCREEN_W/2, y=c.SCREEN_H/2-30)
        self.write(arg=f'Lives: {self.lives}', align='center', font=c.FONT)
        self.goto(x=0, y=c.SCREEN_H/2-30)
        self.write(arg=f'Points: {self.score}', align='center', font=c.FONT)
