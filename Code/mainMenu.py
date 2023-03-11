import pygame
from button import Button
from levelSelct import LevelSelect
from config import mappings,renderText,scaleRect,scaleValue
class MainMenu:
    def __init__(self,screen,width : int,height : int,clock):
        self.height = height
        self.width = width
        buttonTextSize = scaleValue(height,20)
        self.quit = Button((width/2-scaleValue(height,250),height/2+scaleValue(height,100)),scaleRect(self.height,(200,50)),"Quit",pygame.Color(255,0,0),buttonTextSize,pygame.Color(0,0,0))
        self.play = Button((width/2 + scaleValue(height,250),height/2+scaleValue(height,100)),scaleRect(self.height,(200,50)),"Play",pygame.Color(0,255,0),buttonTextSize,pygame.Color(0,0,0))
        self.plus = Button((width/2 + scaleValue(height,100),height/2-scaleValue(height,50)),scaleRect(self.height,(50,50)),"+",pygame.Color(0,255,0),buttonTextSize,pygame.Color(0,0,0))
        self.minus = Button((width/2 - scaleValue(height,100),height/2-scaleValue(height,50)),scaleRect(self.height,(50,50)),"-",pygame.Color(0,255,0),buttonTextSize,pygame.Color(0,0,0))
        self.winnerText = ""
        self.screen = screen
        self.clock = clock
        self.maxPlayers = len(mappings)
        self.playerCount = 2
    
    def update(self,delta : float,gametime : float,levelHandler):
        renderText(self.screen,"Menu","timesnewroman",scaleValue(self.height,100),pygame.Color(255,0,0),(self.width/2 - scaleValue(self.height,130),scaleValue(self.height,20)))
        renderText(self.screen,self.winnerText,"timesnewroman",scaleValue(self.height,30),pygame.Color(0,255,0),(self.width/2 - scaleValue(self.height,170),self.height/2 - scaleValue(self.height,200)))
        renderText(self.screen,f"{self.playerCount}","timesnewroman",scaleValue(self.height,50),pygame.Color(0,255,0),(self.width/2 - scaleValue(self.height,10),self.height/2 - scaleValue(self.height,50)))
        renderText(self.screen,"Players","timesnewroman",scaleValue(self.height,40),pygame.Color(0,255,0),(self.width/2 - scaleValue(self.height,50),self.height/2 - scaleValue(self.height,90)))
        if(self.quit.update(self.screen,gametime)[0]):
            pygame.quit()
        if(self.play.update(self.screen,gametime)[0]):
            levelHandler.setLevel(LevelSelect(self.screen,self.width,self.height,self.clock,self.playerCount))
        if(self.plus.update(self.screen,gametime)[0]):
            if(self.playerCount + 1 <= self.maxPlayers):
                self.playerCount += 1
        if(self.minus.update(self.screen,gametime)[0]):
            if(self.playerCount - 1 >= 2):
                self.playerCount -= 1
        
