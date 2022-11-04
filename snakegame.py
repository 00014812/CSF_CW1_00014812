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

class WallSegment(Block):

    def __init__(self, pos):
        Block. __init__(self)
        self.color = pygame.Color(200, 200, 200)
        self.pos = pos

class Apple(Black):

    def __init__(self):
        Block.__init__(self)
        self.color = pygame.color(255, 0, 0 )
        self.randomize()

    #Place apple in random block position
    def randomize(self):

        for i, widthOrHeight in enumerate(self.pos):
            self.pos[i] = random.choice(range(SQUARE_BLOCK_SIZE, SCREEN_W_H[0] - SQUARE_BLOCK_SIZE,))

class Chainable:

    def draw(self, screen):
        for seg in self.segments:
            seg.draw(screen)

class Wall(Chainable):

    def __init__(self):
        self.segments = []

    #Make segments form around borders

       for x in range(0, SCREEN_W_H[0], SQUARE_BLOCK_SIZE):
          self.segments.append( WallSegment([x, 0]))
          self.segments.append( WallSegment([x, SCREEN_W_H[1] - SQUARE_BLOCK_SIZE]))

       for y in range(SQUARE_BLOCK_SIZE, SCREEN_W_H[1] - SQUARE_BLOCK_SIZE):
          self.segments.append(WallSegment([0, y]))
          self.segments.append(WallSegment([x, SCREEN_W_H[1] - SQUARE_BLOCK_SIZE, y]))

    def checkWallCollision(self, snake):

        rext1 = Rect(snake.head.pos[0], snake.head.pos[1], SQUARE_BLOCK_SIZE, SQUARE_BLOCK_SIZE)

        for seg in self.segments:
            rect2 = Rect(seg.pos[0], seg.pos[1], SQUARE_BLOCK_SIZE, SQUARE_BLOCK_SIZE)
            if checkCollision(rect1, rext2)
                return True

        return False

class Snake(Chainable):

    def __init__(self):
        self.direction = 'right'  #Default to moving right
        self.moveDist = SQUARE_BLOCK_SIZE * Move_SPEED
        self.segments = []
        self.size = 0
        for i in range(2): #Place segments in top left corner
            if i == 0:
                self.segments.append(BodySegment([SQUARE_BLOCK_SIZE,200])) #2 body segments to start
                self.head = self.segments[0] #Set the head segment for the rest of the game
            else:
                self.segments.append( BodySegment([0, 200]))

    def changeDir(self, direction):

        if self.direction == 'right' and direction == 'left':
            pass
        elif self.direction == 'left' and direction == 'right':
            pass
        elif self.direction == 'up' and direction == 'down':
            pass
        elif self.direction == 'down' and direction == 'up':
            pass
        else:
            self.direction = direction

    def checkTailCollision(self):

        for i, seg in enumerate(self.segments):
            if i == 0:
                continue
            rect1 = Rect(self.head.pos[0], self.head.pos[1], SQUARE_BLOCK_SIZE, SQUARE_BLOCK_SIZE)
            rect2 =
