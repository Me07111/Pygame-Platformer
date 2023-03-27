import pygame
from button import Button
from config import scaleRect,scaleValue,renderer
from networkedLevel import NetworkedLevel
class landingPage:
    def __init__(self,screen,width : int,height : int,clock,client):
        self.screen = screen
        self.height = height
        self.width = width
        buttonTextSize = scaleValue(height,20)
        if client.index == 0:
            self.start = Button((width/2 + scaleValue(height,250),height/2+scaleValue(height,100)),scaleRect(self.height,(200,50)),"start",pygame.Color(0,255,0),buttonTextSize,pygame.Color(0,0,0))
        self.quit = Button((width/2-scaleValue(height,250),height/2+scaleValue(height,100)),scaleRect(self.height,(200,50)),"Quit",pygame.Color(255,0,0),buttonTextSize,pygame.Color(0,0,0))
        self.winnerText = ""
        self.clock = clock
        self.client = client
        self.isConn = False

    def update(self,delta : float,gametime : float,levelHandler):
        self.client.sendCommand("landUpd",isStarted = False)
        if(self.quit.update(self.screen,gametime)[0]):
            levelHandler.backToMenu(self.winnerText)
        if(self.client.index == 0):
            if(self.start.update(self.screen,gametime)[0]):
                playerCount = int(self.client.sendCommand("landUpd",isStarted = True))
                if playerCount >= 2:
                    levelHandler.setLevel(NetworkedLevel(self.screen,self.width,self.height,25,self.clock,playerCount,self.client.map,self))
            else:
                self.client.sendCommand("landUpd",isStarted = False)