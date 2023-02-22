import pygame
from bullet import Bullet
class Weapon(pygame.sprite.Sprite):
    def __init__(self,name,imagePath,isPickedUp,inPos,bulletSpeed,bulletImagePath,fireRate,bulletGravityMultipierl,damage,maxAmmo):
        super().__init__()
        self.name = name
        self.origImage = pygame.image.load(imagePath)
        self.image = self.origImage
        self.isPickedUp = isPickedUp
        self.rect = self.image.get_rect()
        self.rect.center = inPos
        self.showPickUpText = False
        self.bulletSpeed = bulletSpeed
        self.bulletImagePath = bulletImagePath
        self.fireRate = fireRate
        self.fireDelay = 1/(self.fireRate/60)
        self.lastTimeShot = self.fireDelay
        self.bulGravMul = bulletGravityMultipierl
        self.damage = damage
        self.maxAmmo = maxAmmo
        self.ammo = self.maxAmmo

    def shoot(self,direction,level,gameTime,player):
        if(abs(gameTime - self.lastTimeShot) >= self.fireDelay and self.ammo > 0):
            bullet = Bullet(self.bulletSpeed,self.bulletImagePath,self.getMuzzlePos(),direction,self.bulGravMul,self.damage)
            bullet.ignored = player
            level.bullets.add(bullet)
            self.lastTimeShot = gameTime
            self.ammo -= 1
    
    def getMuzzlePos(self):
        return self.rect.center