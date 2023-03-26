import pygame
from button import Button
from config import scaleRect,scaleValue,renderer
from partyClient import PartyClient
from empty import Empty

class partyJoinUi:
    def __init__(self,screen,width : int,height : int,clock):
        self.screen = screen
        self.height = height
        self.width = width
        buttonTextSize = scaleValue(height,20)
        self.quit = Button((width/2-scaleValue(height,250),height/2+scaleValue(height,100)),scaleRect(self.height,(200,50)),"Quit",pygame.Color(255,0,0),buttonTextSize,pygame.Color(0,0,0))
        self.create = Button((width/2 + scaleValue(height,250),height/2+scaleValue(height,100)),scaleRect(self.height,(200,50)),"Create",pygame.Color(0,255,0),buttonTextSize,pygame.Color(0,0,0))
        self.join = Button((width/2,height/2+scaleValue(height,400)),scaleRect(self.height,(200,50)),"Join",pygame.Color(0,255,0),buttonTextSize,pygame.Color(0,0,0))
        self.winnerText = ""
        self.clock = clock
        self.client = Empty()
        self.client.__class__ = PartyClient
        self.isConn = False
        self.isInited = False
    
    def update(self,delta : float,gametime : float,levelHandler):
        if(not self.isInited):
            self.client.__init__("192.168.1.197",12345)
            self.isInited = True
        renderer.renderText(self.screen,self.winnerText,"timesnewroman",scaleValue(self.height,30),pygame.Color(0,255,0),(self.width/2 - scaleValue(self.height,170),self.height/2 - scaleValue(self.height,200)))
        if(self.quit.update(self.screen,gametime)[0]):
            levelHandler.backToMenu(self.winnerText)
        if(self.create.update(self.screen,gametime)[0]):
            print(self.client.makeParty("party",[]))
            self.isConn = True
        if(self.join.update(self.screen,gametime)[0]):
            self.client.connectToParty("party")
        elif(self.isConn):
            print(self.client.sendUpdToServer([True,False,False,False,True]))