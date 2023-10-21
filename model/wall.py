from model.brick import *
import constants as c


class Wall:
    def __init__(self):
        self.bricks = []
        self.create_bricks()

    def create_bricks(self):
        x = -c.SCREEN_H/2 + c.BRICK_GAP + c.BRICK_W/2
        for i in range(0,14):
            y = c.SCREEN_H / 2 - c.UPPER_GAP
            for brick_type in [RedBrick, OrangeBrick, GreenBrick, YellowBrick]:
                for _ in range(0, 2):
                    brick = brick_type()
                    brick.goto(x, y)
                    self.bricks.append(brick)
                    y -= (c.BRICK_GAP + 10)
            x += c.BRICK_GAP + c.BRICK_W
