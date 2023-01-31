import pygame
from level import Level
pygame.init()
# Set up the drawing window
width = 500
height = 500
screen = pygame.display.set_mode([width, height])
clock = pygame.time.Clock()
Framerate  = 60

# Run until the user asks to quit

currentLevel = Level(screen,width,height,10)
currentLevel.setup()
running = True
while running:

    # Did the user click the window close button?
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((255, 255, 255))
    # Fill the background with white
    delta = clock.tick(60) / 1000
    currentLevel.update(delta)
    # Flip the display
    pygame.display.flip()

# Done! Time to quit.
pygame.quit()