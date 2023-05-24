import pygame
from config import renderer
class Button:
    def __init__(self,pos : tuple,size : tuple,text : str,color = pygame.Color(255,255,255),textSize : int = 20,textColor = pygame.Color(0,0,0),hoveredColor = pygame.Color(0,0,0,50),pressedColor = pygame.Color(0,0,0),cooldown : float = 0.1):
        super().__init__()
        pygame.init()
        self.rect = pygame.Rect(pos,size)
        self.rect.center = pos
        self.color = color
        self.hoveredColor = hoveredColor
        self.pressedColor = pressedColor
        self.text = text
        self.textSize = textSize
        self.textColor = textColor
        self.cooldown = cooldown
        self.lastTimePressed = -cooldown
    
    def update(self,screen,gameTime : float) -> tuple[bool,bool]:
        pygame.init()
        mousePos = pygame.mouse.get_pos()
        if(pygame.Rect.collidepoint(self.rect,mousePos[0],mousePos[1])):
            if(pygame.mouse.get_pressed(3)[0] and gameTime - self.lastTimePressed > self.cooldown):
                self.lastTimePressed = gameTime
                renderer.rects.append((self.pressedColor,self.rect))
                renderer.renderText(screen,self.text,"timesnewroman",self.textSize,self.textColor,(self.rect.centerx - 20,self.rect.centery))
                return (True,True)
            else:
                renderer.rects.append((self.hoveredColor,self.rect))
                renderer.renderText(screen,self.text,"timesnewroman",self.textSize,self.textColor,(self.rect.centerx - 20,self.rect.centery))
                return (False,True)
                
        else:
            renderer.rects.append((self.color,self.rect))
        renderer.renderText(screen,self.text,"timesnewroman",self.textSize,self.textColor,(self.rect.centerx - 20,self.rect.centery))
        return (False,False)