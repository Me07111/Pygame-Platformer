import pygame
class LevelHandler():
    def __init__(self,initiallevel):
        self.currentLevel = initiallevel

    def update(self,delta,gametime):
        self.currentLevel.update(delta,gametime,self)

    def setLevel(self,level):
        if(level == None):
            pygame.quit()
        self.currentLevel = level