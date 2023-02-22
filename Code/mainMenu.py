import pygame
from level import Level
from button import Button
class MainMenu():
    def __init__(self,screen,level1):
        self.quit = Button((200,200),(200,50),"Quit")
        self.play = Button((500,200),(200,50),"Play")
        self.screen = screen
        self.level1 = level1
    
    def update(self,delta,gametime,levelHandler):
        if(self.quit.update(self.screen)):
            pygame.quit()
        if(self.play.update(self.screen)):
            levelHandler.setLevel(self.level1)
