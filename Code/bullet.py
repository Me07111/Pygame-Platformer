import pygame
from config import scaleRect
class Bullet(pygame.sprite.Sprite):
    def __init__(self,speed,imagePath,pos,dir,gravityMultiplier,damage,height):
        super().__init__()
        image = pygame.image.load(imagePath)
        size = (image.get_rect().width,image.get_rect().height)
        self.OrigImage = pygame.transform.scale(pygame.image.load(imagePath),scaleRect(height,size))
        self.image = self.OrigImage
        self.rect = self.image.get_rect()
        self.rect.center = pos
        self.velocity = dir * speed
        self.gravMul = gravityMultiplier
        self.ignored = None
        self.damage = damage
    def updateRot(self):
        rotation = pygame.math.Vector2.angle_to(pygame.Vector2(0,0),self. velocity)
        self.image = pygame.transform.rotate(self.OrigImage,-rotation)