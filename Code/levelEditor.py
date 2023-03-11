import pygame
from platformBase import PlatformBase
from button import Button
from config import scaleRect, incDecInt, weapons, maps
class LevelEditor: 
    def __init__(self,mapSize : tuple[int,int],height : int ,screen : pygame.Surface,loaded : int = -1,):
        if(loaded == -1):
            self.map = []
            for i in range(mapSize[0]):
                row = []
                for j in range(mapSize[1]):
                    row.append("o")
                self.map.append(row)
        else:
            self.map = maps[loaded]
        
        self.cellSize = ()
        self.blockType = "x"
        self.weaponType = 0
        self.typeButton = Button(scaleRect(height,(100,100)),scaleRect(height,(300,50)),"change type")
        self.weaponTypeButton = Button(scaleRect(height,(100,200)),scaleRect(height,(300,50)),"change weapon type")
        self.screen = screen
        self.height = height
        self.width = self.height/9*16
        self.cellHeight = self.height/mapSize[1]
        self.cellWidth = self.width/mapSize[0]
        self.cellSize = (self.cellWidth,self.cellHeight)
        self.highlightedSquarePic = pygame.transform.smoothscale(pygame.image.load("Graphics/outline.png"),self.cellSize)
        self.platformImage = pygame.transform.smoothscale(pygame.image.load("Graphics/Platform.png"),self.cellSize)
        self.playerimage = pygame.transform.smoothscale(pygame.image.load("Graphics/Character.png"),self.cellSize)

    def update(self,delta : float,gametime : float,levelHandler):
        mousePos = pygame.mouse.get_pos()
        mapArrayCoord = (int(mousePos[0]//self.cellSize[0]),int(mousePos[1]//self.cellSize[1]))
        typeButtonPressed = self.typeButton.update(self.screen,gametime)
        wepaponTypeButtonPressed = self.weaponTypeButton.update(self.screen,gametime)
        if(typeButtonPressed):
            self.incType()
        elif(wepaponTypeButtonPressed):
            self.weaponType = incDecInt(self.weaponType,1,len(weapons))
        elif(pygame.mouse.get_pressed()[0]):
            if(self.blockType == "w"):
                self.map[mapArrayCoord[0]][mapArrayCoord[1]] = f"{self.blockType}{self.weaponType}"
            else:
                print(mapArrayCoord)
                self.map[mapArrayCoord[0]][mapArrayCoord[1]] = self.blockType
        else:
            pos = (mapArrayCoord[0]*self.cellSize[0],mapArrayCoord[1]*self.cellSize[1])
            rect = pygame.Rect(pos,self.cellSize)
            self.screen.blit(self.highlightedSquarePic,rect)
        self.display()
            
    

    def display(self):
        for i, row in enumerate(self.map):
            for j, cell in enumerate(row):
                pos = (i*self.cellWidth,j*self.cellHeight)
                if(cell == "o"):
                    continue
                elif(cell == "x"):
                    rect = pygame.Rect(pos,self.cellSize)
                    self.screen.blit(self.platformImage,rect)
                elif(cell == "P"):
                    rect = pygame.Rect(pos,self.cellSize)
                    self.screen.blit(self.playerimage,rect)
                elif(cell[0] == "w"):
                    self.weapons.append(pos)


    def incType(self):
        if(self.blockType == "o"):
            self.blockType = "x"
        elif(self.blockType == "x"):
            self.blockType = "P"
        elif(self.blockType == "P"):
            self.blockType = "w"
        elif(self.blockType == "w"):
            self.blockType = "o"