import pygame
class Bullet(pygame.sprite.Sprite):
    def __init__(self,speed,imagePath,pos,dir,gravityMultiplier,damage):
        super().__init__()
        self.OrigImage = pygame.image.load(imagePath)
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