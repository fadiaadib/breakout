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

    def reset_lives(self):
        self.lives = c.LIVES
        self.show()

    def show(self):
        self.clear()
        self.goto(x=60 - c.SCREEN_WIDTH / 2, y=c.SCREEN_HEIGHT / 2 - 30)
        self.write(arg=f'Lives: {self.lives}', align='center', font=c.FONT)
        self.goto(x=0, y=c.SCREEN_HEIGHT / 2 - 30)
        self.write(arg=f'Points: {self.score}', align='center', font=c.FONT)

    def update_score(self, points):
        self.score += points
        self.show()

    def update_lives(self, life):
        self.lives += life
        self.show()

    def out_of_lives(self):
        return self.lives == 0

    def game_over(self):
        self.goto(x=0, y=0)
        self.write(arg=f'Game Over!', align='center', font=c.BIG_FONT)
        self.goto(x=0, y=-25)
        self.write(arg=f'Your Final Score is {self.score}', align='center', font=c.FONT)
