import pygame
from bullet import Bullet
from config import scaleRect
class Weapon(pygame.sprite.Sprite):
    def __init__(self,name : str,imagePath : str,isPickedUp : bool,inPos : tuple,bulletSpeed : int,bulletImagePath : str,fireRate : int,bulletGravityMultipierl : float,damage : float,maxAmmo : int,isFullAuto : bool,offsets,muzzleDist,angle : float,bulletAmount : int,soundPath : str,height : int):
        super().__init__()
        self.name = name
        size = (pygame.image.load(imagePath).get_rect().width/2,pygame.image.load(imagePath).get_rect().height/2)
        self.origImage = pygame.transform.smoothscale(pygame.image.load(imagePath),scaleRect(height,size)) 
        self.image = self.origImage
        self.isPickedUp = isPickedUp
        self.rect = self.image.get_rect()
        self.rect.center = inPos
        self.showPickUpText = False
        self.bulletSpeed = bulletSpeed
        self.bulletImagePath = bulletImagePath
        self.fireRate = fireRate
        self.fireDelay = 1/(self.fireRate/60)
        self.lastTimeShot = -self.fireDelay
        self.bulGravMul = bulletGravityMultipierl
        self.damage = damage
        self.maxAmmo = maxAmmo
        self.ammo = self.maxAmmo
        self.wasShotReleased = True
        self.isFullAuto = isFullAuto
        self.offsets = offsets
        self.muzzleDist = muzzleDist
        self.rotation = 0
        self.isFlipped = False
        self.angle = angle
        self.bulletAmount = bulletAmount
        self.sound = pygame.mixer.Sound(soundPath)
        self.height = height

    def shoot(self,direction : tuple,level,gameTime : float,player):
        if(self.canShoot(gameTime)):
            for i in range(self.bulletAmount):
                direction = pygame.Vector2.rotate(direction,-self.angle/4 + i*(self.angle/self.bulletAmount))
                bullet = Bullet(self.bulletSpeed,self.bulletImagePath,self.getMuzzlePos(),direction,self.bulGravMul,self.damage,player.height)
                bullet.ignored = player
                level.bullets.add(bullet)
                self.lastTimeShot = gameTime
            self.sound.play()
            self.ammo -= 1
            self.wasShotReleased = False
    
    def getMuzzlePos(self):
        #return self.rect.center
        selfPosVect = pygame.Vector2(self.rect.center)
        rotation = self.rotation
        if(self.isFlipped):
            offset = pygame.Vector2(-self.muzzleDist.x,self.muzzleDist.y) 
            offset = offset.rotate(rotation)
        else:
            offset = pygame.Vector2.rotate(self.muzzleDist,rotation)
        return selfPosVect + offset

    
    def canShoot(self,gameTime : float):
        if(self.isFullAuto):
            return abs(gameTime - self.lastTimeShot) >= self.fireDelay and self.ammo > 0
        else:
            return abs(gameTime - self.lastTimeShot) >= self.fireDelay and self.ammo > 0 and self.wasShotReleased
