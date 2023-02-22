import pygame
from level import Level
from button import Button
class MainMenu():
    def __init__(self,screen,width,height,clock):
        self.quit = Button((200,200),(200,50),"Quit")
        self.play = Button((500,200),(200,50),"Play")
        self.screen = screen
        self.width = width
        self.height = height
        self.clock = clock
    
    def update(self,delta,gametime,levelHandler):
        if(self.quit.update(self.screen)):
            pygame.quit()
        if(self.play.update(self.screen)):
            levelHandler.setLevel(Level(self.screen,self.width,self.height,25,self.clock,2,0))
