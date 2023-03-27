import pygame
from button import Button
from config import scaleRect,scaleValue,renderer
from partyClient import PartyClient
from numberPicker import NumberPicker
from saveHandler import SaveHandler
from landingPage import landingPage

class partyJoinUi:
    def __init__(self,screen,width : int,height : int,clock):
        self.screen = screen
        self.height = height
        self.width = width
        buttonTextSize = scaleValue(height,20)
        self.quit = Button((width/2-scaleValue(height,250),height/2+scaleValue(height,100)),scaleRect(self.height,(200,50)),"Quit",pygame.Color(255,0,0),buttonTextSize,pygame.Color(0,0,0))
        self.create = Button((width/2 + scaleValue(height,250),height/2+scaleValue(height,100)),scaleRect(self.height,(200,50)),"Create",pygame.Color(0,255,0),buttonTextSize,pygame.Color(0,0,0))
        self.join = Button((width/2,height/2+scaleValue(height,400)),scaleRect(self.height,(200,50)),"Join",pygame.Color(0,255,0),buttonTextSize,pygame.Color(0,0,0))
        self.mapPicker = NumberPicker(self.screen,1,13,(width/2,height/4),(200,50))
        self.winnerText = ""
        self.clock = clock
        self.client = PartyClient("192.168.1.197",12345)
        self.isConn = False
        self.mapIndex = 0
        self.saveHandler = SaveHandler()
    
    def update(self,delta : float,gametime : float,levelHandler):
        if(not self.isConn):
            self.client.connectToServer()
            self.isConn = True
        renderer.renderText(self.screen,self.winnerText,"timesnewroman",scaleValue(self.height,30),pygame.Color(0,255,0),(self.width/2 - scaleValue(self.height,170),self.height/2 - scaleValue(self.height,200)))
        self.mapIndex = self.mapPicker.update(gametime)[0] -1 
        if(self.quit.update(self.screen,gametime)[0]):
            levelHandler.backToMenu(self.winnerText)
        if(self.create.update(self.screen,gametime)[0]):
            map = self.saveHandler.loadMap(self.mapIndex)
            if(self.client.makeParty("party",map) == False):
                levelHandler.backToMenu("Server disconnected")
            elif(self.client.makeParty("party",map).split(" ")[0] == "Succsessfully"):
                levelHandler.setLevel(landingPage(self.screen,self.width,self.height,self.clock,self.client))
            self.isConn = True
        if(self.join.update(self.screen,gametime)[0]):
            if(self.client.connectToParty("party") == False):
                levelHandler.backToMenu("Server disconnected")