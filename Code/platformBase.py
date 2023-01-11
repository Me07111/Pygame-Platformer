import pygame
class platformBase(pygame.sprite.Sprite):
    def __init__(self,InPos,width,height,color):
        self.image = pygame.image.load()
        self.color = color