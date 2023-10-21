from model.brick import *
import constants as c


class Wall:
    def __init__(self):
        self.bricks = []
        self.create_bricks()

    def create_bricks(self):
        x = -c.SCREEN_HEIGHT / 2 + c.BRICK_GAP + c.BRICK_WIDTH / 2
        for i in range(0, c.BRICK_COUNT):
            y = c.SCREEN_HEIGHT / 2 - c.BRICK_UPPER_GAP
            for brick_type in [RedBrick, OrangeBrick, GreenBrick, YellowBrick]:
                for _ in range(0, c.BRICK_REP):
                    brick = brick_type()
                    brick.goto(x, y)
                    self.bricks.append(brick)
                    y -= (c.BRICK_GAP + c.BRICK_HEIGHT)
            x += c.BRICK_GAP + c.BRICK_WIDTH
