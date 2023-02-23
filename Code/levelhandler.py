import pygame
class LevelHandler:
    def __init__(self,menu):
        self.mainMenu = menu
        self.currentLevel = menu

    def update(self,delta,gametime):
        self.currentLevel.update(delta,gametime,self)

    def setLevel(self,level):
        if(level == None):
            pygame.quit()
        self.currentLevel = level

    def backToMenu(self):
        self.setLevel(self.mainMenu)