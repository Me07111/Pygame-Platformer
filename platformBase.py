import pygame
class platformBase:
    def __init__(self,InPos,width,height,color):
        self.rect = pygame.Rect(InPos,width,height)
        self.color = color