from config import renderText
import pygame
class Logger:
    def __init__(self,screen : pygame.Surface):
        self.screen = screen
        self.timeSinceLogged = 1000
        self.timeToLogFor = 1
        self.logText = ""
        self.color = pygame.Color(0,0,0)
        self.pos = (0,0)
        self.size = (100,20)

    def update(self,deltaTime : float):
        self.timeSinceLogged += deltaTime
        if(self.timeSinceLogged < self.timeToLogFor):
            renderText(self.screen,self.logText,"timesnewroman",self.size,self.color,self.pos)

    def log(self,text : str,pos,timeToLogFor : int = 1,color : pygame.Color = pygame.Color(0,0,0),size : tuple = (100,20)):
        self.timeSinceLogged = 0
        self.logText = text
        self.pos = pos
        self.timeToLogFor = timeToLogFor
        self.color = color
        self.size = size