import pygame
from button import Button
from config import scaleRect,scaleValue,renderer
from partyClient import PartyClient
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
        if(self.quit.update(self.screen,gametime)[0]):
            levelHandler.backToMenu(self.winnerText)
        if(self.client.index == 0):
            if(self.create.update(self.screen,gametime)[0]):
                self.client.startGame()
            
        elif(self.isConn):
            print(self.client.sendUpdToServer([True,False,False,False,True]))