import pygame
from button import Button
from levelSelct import LevelSelect
from config import mappings,renderText,scaleRect,scaleValue
class MainMenu:
    def __init__(self,screen,width,height,clock):
        self.height = height
        self.width = height
        self.quit = Button((width/2-200-50,height/2+100)),(200,50),"Quit",pygame.Color(255,0,0),20,pygame.Color(0,0,0)
        self.play = Button((width/2 + 250,height/2+100)),(200,50),"Play",pygame.Color(0,255,0),20,pygame.Color(0,0,0)
        self.plus = Button((width/2 + 100,height/2-50)),(50,50),"+",pygame.Color(0,255,0),20,pygame.Color(0,0,0)
        self.minus = Button((width/2 - 100,height/2-50)),(50,50),"-",pygame.Color(0,255,0),20,pygame.Color(0,0,0)
        self.winnerText = ""
        self.screen = screen
        self.clock = clock
        self.maxPlayers = len(mappings)
        self.playerCount = 2
    
    def update(self,delta,gametime,levelHandler):
        renderText(self.screen,"Menu","timesnewroman",100,pygame.Color(255,0,0),(self.width/2 - 130,20))
        renderText(self.screen,self.winnerText,"timesnewroman",30,pygame.Color(0,255,0),(self.width/2 - 170,self.height/2 - 200))
        renderText(self.screen,f"{self.playerCount}","timesnewroman",50,pygame.Color(0,255,0),(self.width/2 - 10,self.height/2 - 50))
        renderText(self.screen,"Players","timesnewroman",40,pygame.Color(0,255,0),(self.width/2 - 50,self.height/2 - 90))
        if(self.quit.update(self.screen,gametime)):
            pygame.quit()
        if(self.play.update(self.screen,gametime)):
            levelHandler.setLevel(LevelSelect(self.screen,self.width,self.height,self.clock,self.playerCount))
        if(self.plus.update(self.screen,gametime)):
            if(self.playerCount + 1 <= self.maxPlayers):
                self.playerCount += 1
        if(self.minus.update(self.screen,gametime)):
            if(self.playerCount - 1 >= 2):
                self.playerCount -= 1
        
