import pygame
from bullet import Bullet
class Weapon(pygame.sprite.Sprite):
    def __init__(self,name,imagePath,isPickedUp,inPos,bulletSpeed,bulletImagePath,fireRate):
        super().__init__()
        self.name = name
        self.image = pygame.image.load(imagePath)
        self.isPickedUp = isPickedUp
        self.rect = self.image.get_rect()
        self.rect.center = inPos
        self.showPickUpText = False
        self.bulletSpeed = bulletSpeed
        self.bulletImagePath = bulletImagePath
        self.fireRate = fireRate
        self.fireDelay = 1/(self.fireRate/60)
        self.lastTimeShot = self.fireDelay

    def shoot(self,direction,level,gameTime):
        if(abs(gameTime - self.lastTimeShot) >= self.fireDelay):
            bullet = Bullet(self.bulletSpeed,self.bulletImagePath,self.getMuzzlePos(),direction)
            level.bullets.add(bullet)
            self.lastTimeShot = gameTime
    
    def getMuzzlePos(self):
        return self.rect.center