# Classic Snake Game!
# import ...
# Globals

SCREEN_W_H = 1200, 1200

FPS = 60.0

# Controls speed of snake movement

Move_SPEED = 1
NUM_FRAMES_TO_DELAY_MOVE = 3

APPLE_COLOR = pygame.Color(255, 0, 0)  # color is red
SNAKE_COlOR = pygame.Color(0, 255, 0)  # color is green

SQUARE_BLOCK_SIZE = 50

class Block:

    def __init__(self):
        self.color = pygame.Color(0, 0, 0)  # Default color
        self.squareSize = SQUARE_BLOCK_SIZE
        self.pos = [0, 0]  # DEfault pose

    def draw(self, screen):
        rect = Rect(self.pos[0], self.pos[1], SQUARE_BLOCK_SIZE, SQUARE_BLOCK_SIZE)
        screen.fill(self.color, rect)

class BodySegment(Block):

    def __init__(self, pos):
        Block. __init__(self)
        self.color = pygame.Color(0, 255, 0)
        self.pos = pos

    def move(self, newPos):
        self.pos=newPos

class