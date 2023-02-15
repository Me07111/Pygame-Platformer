import pygame
class Bullet(pygame.sprite.Sprite):
    def __init__(self,speed,size,imagePath,pos):
        super().__init__()
        self.speed = speed
        self.image = pygame.image.load(imagePath)
        self.rect = self.image.get_rect()
        self.rect.center = pos