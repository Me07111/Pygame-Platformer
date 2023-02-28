import pygame
from button import Button
from levelSelct import LevelSelect
from config import renderText
class MainMenu:
    def __init__(self,screen,width,height,clock):
        self.quit = Button((width/2-200-50,height/2-50),(200,50),"Quit",pygame.Color(255,0,0),20,pygame.Color(0,0,0))
        self.play = Button((width/2 + 250,height/2-50),(200,50),"Play",pygame.Color(0,255,0),20,pygame.Color(0,0,0))
        self.winnerText = ""
        self.screen = screen
        self.width = width
        self.height = height
        self.clock = clock
        self.playerCount = 2
    
    def update(self,delta,gametime,levelHandler):
        renderText(self.screen,"Menu","timesnewroman",100,pygame.Color(255,0,0),(self.width/2 - 130,20))
        renderText(self.screen,self.winnerText,"timesnewroman",30,pygame.Color(0,255,0),(self.width/2 - 170,self.height/2 - 200))
        if(self.quit.update(self.screen)):
            pygame.quit()
        if(self.play.update(self.screen)):
            levelHandler.setLevel(LevelSelect(self.screen,self.width,self.height,self.clock,self.playerCount))
