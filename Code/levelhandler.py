import pygame
from logger import Logger
class LevelHandler:
    def __init__(self,menu,screen):
        self.mainMenu = menu
        self.currentLevel = menu
        self.logger = Logger(screen)

    def update(self,delta : float,gametime : float):
        self.currentLevel.update(delta,gametime,self)
        self.logger.update(delta)

    def setLevel(self,level):
        if(level == None):
            pygame.quit()
        self.currentLevel = level

    def backToMenu(self,winner : str):
        self.mainMenu.winnerText = f"{winner} won! Another round?"
        self.setLevel(self.mainMenu)