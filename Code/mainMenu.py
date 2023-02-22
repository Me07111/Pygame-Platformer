import pygame
from level import Level
from button import Button
class MainMenu():
    def __init__(self,screen,width,height,clock):
        self.quit = Button((width/2-200-50,height/2-50),(200,50),"Quit",pygame.Color(255,0,0),20,pygame.Color(0,0,0))
        self.play = Button((width/2 + 250,height/2-50),(200,50),"Play",pygame.Color(0,255,0),20,pygame.Color(0,0,0))
        self.screen = screen
        self.width = width
        self.height = height
        self.clock = clock
    
    def update(self,delta,gametime,levelHandler):
        if(self.quit.update(self.screen)):
            #pygame.quit()
            pass
        if(self.play.update(self.screen)):
            levelHandler.setLevel(Level(self.screen,self.width,self.height,25,self.clock,2,0))
