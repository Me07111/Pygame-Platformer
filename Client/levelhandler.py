import pygame
from logger import Logger
import time
class LevelHandler:
    def __init__(self,menu,screen):
        self.mainMenu = menu
        self.currentLevel = menu
        self.logger = Logger(screen)

    def update(self,delta : float,gametime : float):
        self.currentLevel.update(delta,gametime,self)
        self.logger.update(delta)

    def setLevel(self,level):
        print("setlevel callsed")
        if(level == None):
            pygame.quit()
        time.sleep(0.1)
        self.currentLevel = level
        print(self.currentLevel)

    def backToMenu(self,winner : str):
        print("levelHandler.becToMenu Called")
        self.mainMenu.winnerText = f"{winner} won! Another round?"
        self.setLevel(self.mainMenu)