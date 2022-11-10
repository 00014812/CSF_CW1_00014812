<<<<<<< HEAD
# Classic Snake Game !!!

#import ...

# Globals

SCREEN_W_H = 1200, 1200

FPS = 60.0

# Controls speed of snake movement
MOVE_SPEED = 1
NUM_FRAMES_TO_DELAY_MOVE = 3

APPLE_COLOR = pygame.Color (255, 0, 0) # RED
SNAKE_COLOR = pygame.Color (0, 255, 0) #GREEN

SQUARE_BLOCK_SIZE = 50

class Block:

    def __init__(self):
        self.color = pygame.Color (0, 0, 0) # Default color
        self.squareSize = SQUARE_BLOCK_SIZE
        self.pos = [0, 0] # Default pos

    def draw(self, screen):
        rect = Rect(self.pos[0], self.pos[1], SQUARE_BLOCK_SIZE, SQUARE_BLOCK_SIZE)
        screen.fill(self.color, rect)

class BodySegment(Block):

    def __init__(self, pos):
        Block.__init__(self)
        self.color = pygame.Color(0, 255, 0)
        self.pos = pos

    def move(self, newPos):
        self.pos = newPos

class WallSegment(Block):

    def __init__(self, pos):
        Block. __init__(self)
        self.color = pygame.Color (200, 200, 200) # GRAY
        self.pos = pos

class Apple(Block):

    def __init__(self):
        Block.__init__(self)
        self.color = pygame.Color(255, 0, 0) #RED
        self.randomize()

    #Place apple in random block position
    def randomize(self):

        for i, widthOrHeight in enumerate(self.pos)
            self.pos[i] = random.choice(range(SQUARE_BLOCK_SIZE, SCREEN_W_H[0] - SQUARE_BLOCK_SIZE, SQUARE_BLOCK_SIZE))

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
            self.segments.append( WallSegment([SCREEN_W_H[1]] - SQUARE_BLOCK_SIZE) )

        for y in range(SQUARE_BLOCK_SIZE, SCREEN_W_H[1] - SQUARE_BLOCK_SIZE, SQUARE_BLOCK_SIZE)
            self.segments.append( WallSegment([0, y]) )
            self.segments.append( WallSegment([SCREEN_W_H[1] - SQUARE_BLOCK_SIZE, y ]) )

    def checkWallCollision(self, snake):

        rect1 = Rect(snake.head.pos[0], snake.head.pos[1], SQUARE_BLOCK_SIZE, SQUARE_BLOCK_SIZE)

        for seg in self.segments:
            rect2 = Rect(seg.pos[0], seg.pos[1], SQUARE_BLOCK_SIZE, SQUARE_BLOCK_SIZE)
            if CheckCollision(rect1, rect2):
                return True
            return False

class Snake(Chainable):

    def __init__(self):
        self.direction = 'right'   #Default moving right
        self.moveDist = SQUARE_BLOCK_SIZE * MOVE_SPEED
        self.segments = []
        self.size = 0
        for i in range(2):
            # Place segments in top left corner
            if i == 0:
                self.segments.append(BodySegment([SQUARE_BLOCK_SIZE, 200] ) )   # 2 body segments
                self.head = self.segments[0] # Set the head segment for the rest of the game
            else:
                self.segments.append( BodySegment([0, 200]) )

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
            rect1 = Rect(self.head.pos[0], self.head.pos[1], SQUARE_BLOCK_SIZE, SQUARE_BLOCK_SIZE )
            rect2 = Rect(seg.pos[0], seg.pos[1], SQUARE_BLOCK_SIZE, SQUARE_BLOCK_SIZE)
            if checkCollision(rect1, rect2):
                return True
            return False

    def move(self):
        segmentsLen - len(self.segments)
        head = self.segments[0]

        newHeadPos = []

        if self.direction == 'up':
            newHeadPos = [head.pos[0], head.pos[1] - self.moveDist]
        elif self.direction == 'down':
            newHeadPos = [head.pos[0], head.pos[1] + self.moveDist]
        elif.self.direction = 'left':
            newHeadPos = [head.pos[0] - self.moveDist, head.pos[1]]
        else:
            newHeadPos = [head.pos[0] + self.moveDist, head.pos[1]]

        #Save for adding a segment later
        self.tailLastPos = self.segments[segmentsLen - 1].pos

        #Set each segments position to the next segments position in line
        for i in range(sementsLen - 1, 0, -1):
            self.segments[i].move( self.segments[i -1].pos )

        #Finally set head segments to position of new direction move
        self.segments[0].move( newHeadPos )

    def addSegment(self):

        self.segments.append( BodySegment(self.tailLastPos) )
        self.size+=1

def checkCollision(rect1, rect2):

    if rect1.x == rect2.x and rect1.y == rect2.y:
        return True
    else:
        return False

# Move the player's snake based on the string 'direction'
# Can be 'up', 'down', 'left', 'right'
def changeDir(direction, snake):
    snake.ChangeDir(direction)

def setUpFontSurf(snakeSize):
    font = pygame/font/Font('PixelGameFont.ttf', 60)
    surface = font.render('Score: %d' % snakeSize, True, (255, 255, 255), (0, 0, 0))
    return surface

def getGameOverSurf():
    font = pygame.font.Font('PixelGameFont.ttf', 120 )
    surface = font.render('Game Over', True, (255, 255, 255), (0, 0, 0))
    return surface

def setupScreen():
    pygame.init()
    screen = pygame.display.set_mode(SCREEN_W_H)
    return screen

def main():
    screen = setupScreen()
    fillRect= Rect(0, 0 SCREEN_W_H[0], SCREEN_W_H[1])
    screen.fill((255, 0, 0))

    scoreText = setupFontSurf(0)
    scoreRect = scoreText.get.rect()
    scoreRect.x = 100; scoreRect.y = 100

    gameOverSurf = getGameOverSurf()
    gameOverRect = gameOverSurf.get.rect()

    gameOverRect.x = SCREEN_W_H[0] / 2 -gameOverRect.w / 2
    gameOverRect.y = SCREEN_W_H[1] / 2 -gameOverRect.h / 2

    wall = Wall()

    snake = Snake()

    apple = Apple()

    # Mail Loop

    running = True
    framesSinceLastMove = 0
    while(running):

        #framerate cap
        time.sleep( 1.0 / FPS )

        event = pygame.event.poll()

        direction = ''

        if event.type == QUIT:
            running = False
            continue
        elif event.type == KEYDOWN:
            if event.key == K_UP:
                changeDir('up', snake)
            elif event.key == K_DOWN
                changeDir('down', snake)
            elif event.key == K_LEFT:
                changeDir('left', snake)
            elif event.key == K_RIGHT:
                changeDir('right', snake)
            elif event.key == K_ESCAPE:
                running = False
                continue

        # Draw

        scoreText = setupFontSurf(snake.size)

        screen.fill((0, 0, 0))

        screen.blit(scoreText, scoreRect)

        apple.draw(screen)
        snake.draw(screen)

        wall.draw(screen)

        if frameSinceLastMove == NUM_FRAMES_TO_DELAY_MOVE:
            snake.move()
            framesSinceLastMove = 0

        # Check for apple collision
        headRect = Rect(snake.head.pos[0], snake.head.pos[1], SQUARE_BLOCK_SIZE, SQUARE_BLOCK_SIZE)
        appleRect = Rect(apple.pos[0], apple.pos[1], SQUARE_BLOCK_SIZE, SQUARE_BLOCK_SIZE)

        if chechCollision(headRect, appleRect):
            # Apple collected
            apple = Apple() # Make new
            snake.addSegment()

        if snake.checkTailCollision():
            #Collision with tail
            screen.blit(gameOverSurf, gameOverRect)
            pygame.display.update()
            time.sleep(3)
            running = False
            continue

        if wall.checkWallCollision(snake):
            screen.blit(gameOverSurf, gameOverRect)
            pygame.display.update()
            time.sleep(3)
            running = False
            continue

        pygame.display.flip()

        pygamre.display.update()

        framesSinceLastMove+=1

if __name__ == '__main__':
    main()







