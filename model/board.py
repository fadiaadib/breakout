from model.ball import Ball
import constants as c
from helpers import *


class Board:
    def __init__(self):
        self.w = -c.SCREEN_WIDTH / 2
        self.e = c.SCREEN_WIDTH / 2
        self.n = c.SCREEN_HEIGHT / 2
        self.s = -c.SCREEN_HEIGHT / 2
        self.bounce_sound = 'board'
        self.fail_sound = 'life'

    def check_collision(self, ball: Ball):
        w, n, e, s = ball.bounds()

        # if e >= self.e or w <= self.w:
        if e >= self.e or w <= self.w:
            ball.bounce('v')
            audio.play(self.bounce_sound)

        # elif n >= self.n or (c.DEBUG and s <= self.s):
        elif n >= self.n or (c.DEBUG and s <= self.s):
            ball.bounce('h')
            audio.play(self.bounce_sound)

        elif n <= self.s:
            # Lose life:
            audio.play(self.fail_sound)
            return False

        return True
