# Screen attributes
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 800
TITLE = 'Breakout!'

# Turtle
CONV = 20

# Ball
BALL_SIZE = 0.5
BALL_SPEED = 5
BALL_ORIENT = (210, 330)
BALL_SPEED_INC = 1

# Paddle
PADDLE_WIDTH = 300
PADDLE_HEIGHT = 10
PADDLE_SPEED = 100
PADDLE_SOUTH_GAP = 30

# Brick Wall
BRICK_UPPER_GAP = 120
BRICK_REP = 2
BRICK_COUNT = 14
BRICK_GAP = 10
BRICK_HEIGHT = 10
BRICK_WIDTH = (SCREEN_WIDTH - BRICK_GAP * 2) / BRICK_COUNT - BRICK_GAP
BRICK_DEAD_COLOR = '#191919'

# Game rules
LIVES = 3

# Colors
BG_COLOR = '#191919'
FONT_COLOR = '#A9A9A9'
PADDLE_COLOR = '#03a1fc'
BALL_COLOR = '#FFFFFF'

# Fonts
FONT = ('Courier', 16, 'normal')
BIG_FONT = ('Courier', 24, 'bold')

# Debug
DEBUG = False
SOUND_ON = True
