import pygame
class PlatformBase(pygame.sprite.Sprite):
    def __init__(self,InPos,width,height,color):
        self.image = pygame.image.load()
        self.color = color
        self.image = pygame.transform.scale(pygame.image.load("..Graphics/Character.png").fill(color),(width,height))
        self.rect = self.image.get_rect()
        self.rect.center = InPos