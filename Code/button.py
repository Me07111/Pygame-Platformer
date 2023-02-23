import pygame
from config import renderText
class Button:
    def __init__(self,pos,size,text,color = pygame.Color(255,255,255),textSize = 20,textColor = pygame.Color(0,0,0),hoveredColor = pygame.Color(0,0,0,50),pressedColor = pygame.Color(0,0,0)):
        super().__init__()
        self.rect = pygame.Rect(pos,size)
        self.rect.center = pos
        self.color = color
        self.hoveredColor = hoveredColor
        self.pressedColor = pressedColor
        self.text = text
        self.textSize = textSize
        self.textColor = textColor
    
    def update(self,screen):
        mousePos = pygame.mouse.get_pos()
        if(pygame.Rect.collidepoint(self.rect,mousePos[0],mousePos[1])):
            if(pygame.mouse.get_pressed(3)[0]):
                pygame.draw.rect(screen,self.pressedColor,self.rect)
                return True
            else:
                pygame.draw.rect(screen,self.hoveredColor,self.rect)
        else:
            pygame.draw.rect(screen,self.color,self.rect)
        renderText(screen,self.text,"timesnewroman",self.textSize,self.textColor,(self.rect.centerx - 20,self.rect.centery))
        return False