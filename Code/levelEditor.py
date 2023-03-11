import pygame
from button import Button
from config import scaleRect, incDecInt, weapons, renderText
class LevelEditor: 
    def __init__(self,mapSize : tuple[int,int],height : int ,screen : pygame.Surface,saveHandler,slotIndex : int,loaded : int = -1):
        if(loaded == -1):
            self.map = []
            for i in range(mapSize[1]):
                row = []
                for j in range(mapSize[0]):
                    row.append("o")
                self.map.append(row)
        else:
            self.map = saveHandler.loadMap(loaded)
        
        self.slotIndex = slotIndex
        self.saveHandler = saveHandler
        self.cellSize = ()
        self.blockType = "x"
        self.weaponType = 0
        self.typeButton = Button(scaleRect(height,(100,50)),scaleRect(height,(200,50)),"change type")
        self.weaponTypeButton = Button(scaleRect(height,(100,150)),scaleRect(height,(300,50)),"change weapon type")
        self.quitButton = Button(scaleRect(height,(1180,50)),scaleRect(height,(200,50)),"Quit(noSave)")
        self.saveButton = Button(scaleRect(height,(1180,150)),scaleRect(height,(200,50)),"Save")
        self.slotIndexPlusButton = Button(scaleRect(height,(1070,50)),scaleRect(height,(50,50)),"+")
        self.slotIndexMinusButton = Button(scaleRect(height,(870,50)),scaleRect(height,(50,50)),"-")
        self.screen = screen
        self.height = height
        self.width = self.height/9*16
        self.cellHeight = self.height/mapSize[1]
        self.cellWidth = self.width/mapSize[0]
        self.cellSize = (self.cellWidth,self.cellHeight)
        self.highlightedSquarePic = pygame.transform.smoothscale(pygame.image.load("Graphics/outline.png"),self.cellSize)
        self.platformImage = pygame.transform.smoothscale(pygame.image.load("Graphics/Platform.png"),self.cellSize)
        self.playerimage = pygame.transform.smoothscale(pygame.image.load("Graphics/Character.png"),self.cellSize)
        self.weaponImages = []
        for weapon in weapons:
            self.weaponImages.append(pygame.transform.smoothscale(pygame.image.load(weapon[1]),self.cellSize))
        self.timeSincePressed = 10

    def update(self,delta : float,gametime : float,levelHandler):
        mousePos = pygame.mouse.get_pos()
        mapArrayCoord = (int(mousePos[0]//self.cellSize[0]),int(mousePos[1]//self.cellSize[1]))
        typeButtonPressed = self.typeButton.update(self.screen,gametime)
        if(self.blockType == "w"):
            wepaponTypeButtonPressed = self.weaponTypeButton.update(self.screen,gametime)
        else:
            wepaponTypeButtonPressed = (False,False)
        saveButtonPressed = self.saveButton.update(self.screen,gametime)
        quitButtonPressed = self.quitButton.update(self.screen,gametime)
        saveIndexPlusButtonPressed = self.slotIndexPlusButton.update(self.screen,gametime)
        saveIndexMinusButtonPressed = self.slotIndexMinusButton.update(self.screen,gametime)
        isButtonHovered = typeButtonPressed[1] or wepaponTypeButtonPressed[1] or saveButtonPressed[1] or quitButtonPressed[1] or saveIndexPlusButtonPressed[1] or saveIndexMinusButtonPressed[1]
        if(typeButtonPressed[0]):
            self.incType()
        elif(wepaponTypeButtonPressed[0]):
            self.weaponType = incDecInt(self.weaponType,1,len(weapons) - 1)
        elif(saveButtonPressed[0]):
            if(self.checkCanSave()):
                self.saveHandler.saveMap(self.map, self.slotIndex)
                levelHandler.logger.log("Saved Successfully",(self.width/2-100,50),2,pygame.Color(0,255,0),25)
            else:
                levelHandler.logger.log("Cant Save",(self.width/2-100,50),2,pygame.Color(255,0,0),25)
        elif(quitButtonPressed[0]):
            levelHandler.backToMenu("")
        elif(saveIndexPlusButtonPressed[0]):
            self.slotIndex = incDecInt(self.slotIndex,1,14)
        elif(saveIndexMinusButtonPressed[0]):
            self.slotIndex = incDecInt(self.slotIndex,-1,14)
        elif(isButtonHovered):
            pass
        elif(pygame.mouse.get_pressed()[0]):
            if(self.blockType == "w"):
                self.map[mapArrayCoord[1]][mapArrayCoord[0]] = f"{self.blockType}{self.weaponType}"
            else:
                self.map[mapArrayCoord[1]][mapArrayCoord[0]] = self.blockType
        else:
            pos = (mapArrayCoord[0]*self.cellSize[0],mapArrayCoord[1]*self.cellSize[1])
            rect = pygame.Rect(pos,self.cellSize)
            self.screen.blit(self.highlightedSquarePic,rect)
        self.display()
            
    

    def display(self):
        for i, row in enumerate(self.map):
            for j, cell in enumerate(row):
                pos = (j*self.cellWidth,i*self.cellHeight)
                rect = pygame.Rect(pos,self.cellSize)
                self.displayBlock(cell,rect)
        
        if(self.blockType != "w"):
            cellstr = self.blockType
        else:
            cellstr = self.blockType + str(self.weaponType)
        cellRect = pygame.Rect((220,25),self.cellSize)
        self.displayBlock(cellstr,cellRect)
        renderText(self.screen,f"Map to save to:{self.slotIndex+1}","timesnewroman",20,pygame.Color(0,0,0),(965,45))
                    
    def incType(self):
        if(self.blockType == "o"):
            self.blockType = "x"
        elif(self.blockType == "x"):
            self.blockType = "P"
        elif(self.blockType == "P"):
            self.blockType = "w"
        elif(self.blockType == "w"):
            self.blockType = "o"

    def displayBlock(self,cell : str,rect : pygame.Rect):
        if(cell == "o"):
            pass
        elif(cell == "x"):
            self.screen.blit(self.platformImage,rect)
        elif(cell == "P"):
            self.screen.blit(self.playerimage,rect)
        elif(cell[0] == "w"):
            self.screen.blit(self.weaponImages[int(cell[1])],rect)
    
    def checkCanSave(self) -> bool:
        return self.getPlayerCount() >= 2
    
    def getPlayerCount(self) -> int:
        players = 0
        for row in self.map:
            for cell in row:
                if(cell == "P"):
                    players += 1
        return players
        