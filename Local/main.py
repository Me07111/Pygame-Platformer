import pygame
from mainMenu import MainMenu
from levelhandler import LevelHandler
from renderer import Renderer
from config import renderer
pygame.init()
pygame.font.init()
# Set up the drawing window
displayInfo = pygame.display.Info()
if(displayInfo.current_w < displayInfo.current_h / 9 * 16):
    width = displayInfo.current_w
    height = width / 16 * 9
else:
    height = displayInfo.current_h
    width = height / 9 * 16
screen = pygame.display.set_mode([width, height])
clock = pygame.time.Clock()
Framerate  = 60
#time passed since the game has started in seconds
gameTime = 0
# Run until the user asks to quit
renderer.screen = screen
mainMenu = MainMenu(screen,width,height,clock)
levelHandler = LevelHandler(mainMenu,screen)
running = True
while running:
    # Did the user click the window close button?
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((200, 200, 200))
    # Fill the background with white
    delta = clock.tick(60) / 1000
    gameTime += delta
    levelHandler.update(delta,gameTime)
    renderer.update()
    # Flip the display
    pygame.display.flip()
# Done! Time to quit.
pygame.quit()