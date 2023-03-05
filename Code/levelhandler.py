import pygame
class LevelHandler:
    def __init__(self,menu):
        self.mainMenu = menu
        self.currentLevel = menu

    def update(self,delta : float,gametime : float):
        self.currentLevel.update(delta,gametime,self)

    def setLevel(self,level):
        if(level == None):
            pygame.quit()
        self.currentLevel = level

    def backToMenu(self,winner : str):
        self.mainMenu.winnerText = f"{winner} won! Another round?"
        self.setLevel(self.mainMenu)