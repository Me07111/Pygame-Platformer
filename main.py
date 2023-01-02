import pygame
from player import Character
pygame.init()

width = 500
height = 500
# Set up the drawing window
screen = pygame.display.set_mode([width, height])

player1 = Character(pygame.Vector2(width/2, height/2),pygame.color(255,0,0,255),screen,20,50)
# Run until the user asks to quit
running = True
while running:

    # Did the user click the window close button?
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    player1.update(pygame.time.get_ticks())

    # Fill the background with white
    screen.fill((255, 255, 255))

    # Draw a solid blue circle in the center
    pygame.draw.circle(screen, (0, 0, 255), player1.pos, 75)

    # Flip the display
    pygame.display.flip()

# Done! Time to quit.
pygame.quit()