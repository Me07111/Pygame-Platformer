import pygame
from button import Button
from levelSelct import LevelSelect
from config import mappings,scaleRect,scaleValue,renderer
from numberPicker import NumberPicker
class MainMenu:
    def __init__(self,screen,width : int,height : int,clock):
        pygame.init()
        self.screen = screen
        self.height = height
        self.width = width
        buttonTextSize = scaleValue(height,20)
        self.quit = Button((width/2-scaleValue(height,250),height/2+scaleValue(height,100)),scaleRect(self.height,(200,50)),"Quit",pygame.Color(255,0,0),buttonTextSize,pygame.Color(0,0,0))
        self.play = Button((width/2 + scaleValue(height,250),height/2+scaleValue(height,100)),scaleRect(self.height,(200,50)),"Play",pygame.Color(0,255,0),buttonTextSize,pygame.Color(0,0,0))
        self.playerCountPicker = NumberPicker(self.screen,2,4,(int(width/2),scaleValue(height,300)),scaleRect(height,(400,50)))
        self.winnerText = ""
        self.clock = clock
        self.maxPlayers = len(mappings)
        self.playerCount = 2
    
    def update(self,delta : float,gametime : float,levelHandler):
        renderer.renderText(self.screen,"Menu","timesnewroman",scaleValue(self.height,100),pygame.Color(255,0,0),(self.width/2 - scaleValue(self.height,130),scaleValue(self.height,20)))
        renderer.renderText(self.screen,self.winnerText,"timesnewroman",scaleValue(self.height,30),pygame.Color(0,255,0),(self.width/2 - scaleValue(self.height,170),self.height/2 - scaleValue(self.height,200)))
        doQuit = self.quit.update(self.screen,gametime)[0]
        if(doQuit):
            pygame.quit()
        if(self.play.update(self.screen,gametime)[0]):
            levelHandler.setLevel(LevelSelect(self.screen,self.width,self.height,self.clock,self.playerCount))
        self.playerCount = self.playerCountPicker.update(gametime)[0]
        
