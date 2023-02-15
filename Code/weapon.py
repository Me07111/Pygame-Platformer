import pygame
class Weapon(pygame.sprite.Sprite):
    def __init__(self,name,imagePath,isPickedUp,inPos,bulletSpeed,bulletImagePath):
        super().__init__()
        self.name = name
        self.image = pygame.image.load(imagePath)
        self.isPickedUp = isPickedUp
        self.rect = self.image.get_rect()
        self.rect.center = inPos
        self.showPickUpText = False
        self.bulletSpeed = bulletSpeed
        self.bulletImagePath = bulletImagePath
