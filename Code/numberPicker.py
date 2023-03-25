from button import Button
import pygame
from config import incDecInt,renderer
class NumberPicker:
    def __init__(self,screen,minimum,maximum,pos,size,doesDisplayNumber = True,amount = 1) -> None:
        self.screen = screen
        self.min = minimum
        self.max = maximum
        self.value = minimum
        self.pos = pos
        self.size = size
        self.plusButton = Button((pos[0] + size[0] / 6,pos[1]),(size[0]/3,size[1]),"+",pygame.Color(0,255,0),int(size[1]/2))
        self.minusButton = Button((pos[0] - size[0] / 6 * 3,pos[1]),(size[0]/3,size[1]),"-",pygame.Color(255,0,0),int(size[1]/2))
        self.doesDisplayNumber = doesDisplayNumber
        self.amount = amount

    def update(self,gameTime,value = -1) -> int:
        wasPressed = False
        isHovered = False
        minusUpd = self.minusButton.update(self.screen,gameTime)
        plusUpd = self.plusButton.update(self.screen,gameTime)
        if(value != -1):
            self.value = value
            wasPressed = True
        if(minusUpd[1] or plusUpd[1]):
            isHovered = True
        if(minusUpd[0]):
            self.value = incDecInt(self.value,-self.amount,self.max,self.min)
            wasPressed = True
        if(plusUpd[0]):
            self.value = incDecInt(self.value,self.amount,self.max,self.min)
            wasPressed = True
        if(self.doesDisplayNumber):
            renderer.renderText(self.screen,str(self.value),"timesnewroman",int(self.size[1]/2),pygame.Color(0,0,0),(self.pos[0] - self.size[0] / 6,self.pos[1]))
        return self.value,wasPressed,isHovered
