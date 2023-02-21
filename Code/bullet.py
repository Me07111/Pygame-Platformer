import pygame
class Bullet(pygame.sprite.Sprite):
    def __init__(self,speed,imagePath,pos,dir,gravityMultiplier,damage):
        super().__init__()
        self.image = pygame.image.load(imagePath)
        self.rect = self.image.get_rect()
        self.rect.center = pos
        self.velocity = dir * speed
        self.gravMul = gravityMultiplier
        self.ignored = None
        self.damage = damage