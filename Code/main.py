import pygame
from level import Level
from mainMenu import MainMenu
from levelhandler import LevelHandler
pygame.init()
pygame.font.init()
# Set up the drawing window
width = 1280
height = 720
screen = pygame.display.set_mode([width, height])
clock = pygame.time.Clock()
Framerate  = 60
#time passed since the game has started in seconds
gameTime = 0

# Run until the user asks to quit
Level1 = Level(screen,width,height,25,clock,2,0,Level(screen,width,height,50,clock,2,0,MainMenu(screen,None)))
levelHandler = LevelHandler(MainMenu(screen,Level1))
running = True
while running:

    # Did the user click the window close button?
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((255, 255, 255))
    # Fill the background with white
    delta = clock.tick(60) / 1000
    gameTime += delta
    levelHandler.update(delta,gameTime)
    # Flip the display
    pygame.display.flip()

# Done! Time to quit.
pygame.quit()

def setLevel(level):
    currentLevel = level