import pygame
from button import Button
from config import scaleRect, incDecInt, weapons, renderText, powerUps , clip
from numberPicker import NumberPicker
from saveHandler import SaveHandler
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
        self.blockType = 1
        self.blockTypes = ["o","x","P","w","u","L"]
        self.doesHaveSubTypes = ["no","no","no","sub","sub","par"]
        self.parMaxes = [0,0,0,0,0,10000]
        self.subType = 0
        self.quitButton = Button(scaleRect(height,(1180,50)),scaleRect(height,(200,50)),"Quit(noSave)")
        self.saveButton = Button(scaleRect(height,(1180,150)),scaleRect(height,(200,50)),"Save")
        self.slotIndexPlusButton = Button(scaleRect(height,(1070,50)),scaleRect(height,(50,50)),"+")
        self.slotIndexMinusButton = Button(scaleRect(height,(870,50)),scaleRect(height,(50,50)),"-")
        self.loadButton = Button(scaleRect(height,(1180,250)),scaleRect(height,(200,50)),"Load")
        self.screen = screen
        self.height = height
        self.width = self.height/9*16
        self.cellHeight = self.height/mapSize[1]
        self.cellWidth = self.width/mapSize[0]
        self.cellSize = (self.cellWidth,self.cellHeight)
        self.highlightedSquarePic = pygame.transform.smoothscale(pygame.image.load("Graphics/outline.png"),self.cellSize)
        platformImage = pygame.transform.smoothscale(pygame.image.load("Graphics/Platform.png"),self.cellSize)
        playerimage = pygame.transform.smoothscale(pygame.image.load("Graphics/Character.png"),self.cellSize)
        weaponImages = []
        jumpPadImage = pygame.transform.smoothscale(pygame.image.load("Graphics/JumpPad.png"),self.cellSize)
        weaponImages = []
        for weapon in weapons:
            weaponImages.append(pygame.transform.smoothscale(pygame.image.load(weapon[1]),self.cellSize))
        powerupImages = []
        for powerUp in powerUps:
            powerupImages.append(pygame.transform.smoothscale(clip(pygame.image.load(powerUp.get("imagePath")),0,0,40,40),self.cellSize))
        self.subImages = [[],[platformImage],[playerimage],weaponImages,powerupImages,[jumpPadImage]]
        self.timeSincePressed = 10
        self.typePicker = NumberPicker(self.screen,0,len(self.blockTypes)-1,scaleRect(height,(140,50)),scaleRect(height,(200,50)),False)
        self.subTypePicker = NumberPicker(self.screen,0,0,scaleRect(height,(220,150)),scaleRect(height,(300,50)),amount=1)
        self.saveHandler = SaveHandler()

    def update(self,delta : float,gametime : float,levelHandler):
        mousePos = pygame.mouse.get_pos()
        mapArrayCoord = (int(mousePos[0]//self.cellSize[0]),int(mousePos[1]//self.cellSize[1]))
        saveButtonPressed = self.saveButton.update(self.screen,gametime)
        quitButtonPressed = self.quitButton.update(self.screen,gametime)
        saveIndexPlusButtonPressed = self.slotIndexPlusButton.update(self.screen,gametime)
        saveIndexMinusButtonPressed = self.slotIndexMinusButton.update(self.screen,gametime)
        newType,typePressed,typeHovered = self.typePicker.update(gametime)
        newSubType,subTypePressed,subTypeHovered = self.subTypePicker.update(gametime)
        loadPressed,LoadHovered = self.loadButton.update(self.screen,gametime)
        isButtonHovered = LoadHovered or subTypeHovered or typeHovered or saveButtonPressed[1] or quitButtonPressed[1] or saveIndexPlusButtonPressed[1] or saveIndexMinusButtonPressed[1]
        if(typePressed):
            self.blockType = newType
            if(self.doesHaveSubTypes[self.blockType] == "sub" or self.doesHaveSubTypes[self.blockType] == "no"):
                self.subTypePicker.max = len(self.subImages[self.blockType]) - 1
                self.subTypePicker.amount = 1
            else:
                self.subTypePicker.max = self.parMaxes[self.blockType]
                self.subTypePicker.amount = 10
        elif(subTypePressed):
            self.subType = newSubType
        elif(saveButtonPressed[0]):
            savedata = self.checkCanSave()
            if(savedata[0]):
                self.saveHandler.saveMap(self.map, self.slotIndex)
                levelHandler.logger.log("Saved Successfully",(self.width/2-100,50),2,pygame.Color(0,255,0),25)
            else:
                levelHandler.logger.log(savedata[1],(self.width/2-100,50),2,pygame.Color(255,0,0),25)
        elif(loadPressed):
            self.map = self.saveHandler.loadMap(self.slotIndex)
        elif(quitButtonPressed[0]):
            levelHandler.backToMenu("")
        elif(saveIndexPlusButtonPressed[0]):
            self.slotIndex = incDecInt(self.slotIndex,1,14)
        elif(saveIndexMinusButtonPressed[0]):
            self.slotIndex = incDecInt(self.slotIndex,-1,14)
        elif(isButtonHovered):
            pass
        elif(pygame.mouse.get_pressed()[0]):
            if(mapArrayCoord[0] >= 0 and mapArrayCoord[1] >= 0 and mapArrayCoord[1] < len(self.map) and mapArrayCoord[0] < len(self.map[0])):
                self.map[mapArrayCoord[1]][mapArrayCoord[0]] = self.typesToString(self.blockType,self.subType)
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
                types = self.stringToTypes(cell)
                self.displayBlock(types[0],types[1],rect)
        
        cellRect = pygame.Rect((90,35),self.cellSize)
        self.displayBlock(self.blockType,self.subType,cellRect)
        renderText(self.screen,f"Map to save to:{self.slotIndex+1}","timesnewroman",20,pygame.Color(0,0,0),(965,45))

    def displayBlock(self,type : int,subtype,rect : pygame.Rect):
        if(type == 0):
            return
        if(self.doesHaveSubTypes[type] == "sub"):
            image = self.subImages[type][subtype]
        else:
            image = self.subImages[type][0]
        self.screen.blit(image,rect)
        
    
    def checkCanSave(self):
        playerCount = self.getBlockCount("P")
        weaponCount = self.getBlockCount("w")
        canSave = playerCount >= 2 and weaponCount >= 1
        if(playerCount < 2):
            massage = "Not enuf players!"
        elif(weaponCount < 1):
            massage = "Not enuf guns!"
        else:
            massage = ""
        return canSave, massage
    
    def getBlockCount(self,str) -> int:
        players = 0
        for row in self.map:
            for cell in row:
                if(cell.startswith(str)):
                    players += 1
        return players

    def typesToString(self,type : int,subType : int) -> str:
        if(self.doesHaveSubTypes[type] == "sub" or self.doesHaveSubTypes[type] == "par"):
            return self.blockTypes[type] + str(subType)     
        else:
            return self.blockTypes[type]

    def stringToTypes(self, string : str):
        if(len(string) < 2):
            return self.blockTypes.index(string[0]),0
        else:
            return self.blockTypes.index(string[0]),int(string[1])