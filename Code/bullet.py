import pygame
from config import scaleRect,scaleValue
class Bullet(pygame.sprite.Sprite):
    def __init__(self,speed : float,imagePath : str,pos,dir,gravityMultiplier : float,damage : float,height : int):
        super().__init__()
        image = pygame.image.load(imagePath)
        size = (image.get_rect().width,image.get_rect().height)
        self.OrigImage = pygame.transform.smoothscale(pygame.image.load(imagePath),scaleRect(height,size))
        self.image = self.OrigImage
        self.rect = self.image.get_rect()
        self.rect.center = pos
        self.velocity = dir * scaleValue(height,speed) 
        self.gravMul = gravityMultiplier
        self.ignored = None
        self.damage = damage
    def updateRot(self):
        rotation = pygame.math.Vector2.angle_to(pygame.Vector2(0,0),self. velocity)
        self.image = pygame.transform.rotate(self.OrigImage,-rotation)