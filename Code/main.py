import pygame
from player import Character
pygame.init()

width = 500
height = 500
# Set up the drawing window
screen = pygame.display.set_mode([width, height])

player1 = Character(pygame.math.Vector2(width/2, height/2),pygame.Color(255,0,0,255),screen,20,50)
# Run until the user asks to quit
running = True
while running:

    # Did the user click the window close button?
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    player1.update(pygame.time.get_ticks())
    player1.draw()

    # Fill the background with white
    screen.fill((255, 255, 255))

    # Flip the display
    pygame.display.flip()

# Done! Time to quit.
pygame.quit()