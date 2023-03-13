from config import scaleRect
import pygame
from animator import Animator
class PowerUp(pygame.sprite.Sprite):
    def __init__(self,height : int,pos,name : str,imagePath : str,modifications : dict,isTimed : bool = False,time : int = 0):
        super().__init__()
        self.height = height
        self.origImage = pygame.image.load(imagePath)
        self.image = pygame.transform.smoothscale(self.origImage,scaleRect(height,(40,40)))
        self.rect = self.image.get_rect()
        self.rect.center = pos
        self.modifications = modifications
        self.animator = Animator([self.origImage],(40,40),[0.1])
        self.isTimed = isTimed
        self.time = time
        self.isPickedUp = False
        self.player = None
        self.timeSincePickUp = 0

    def update(self,delta : float, *args: any, **kwargs: any) -> None:
        super().update(*args, **kwargs)
        if(not self.isPickedUp):
            self.origImage = self.animator.animate(0,delta)
            self.image = pygame.transform.smoothscale(self.origImage,scaleRect(self.height,(40,40)))
        elif(self.isTimed):
            self.timeSincePickUp += delta
            if(self.timeSincePickUp > self.time):
                self.timerDone()
    
    def pickUp(self,player):
        self.isPickedUp = True
        player.maxJumps += self.modifications.get("maxJumps")
        player.jumpSpeed += self.modifications.get("jumpSpeedMod")
        player.speed += self.modifications.get("speedMod")
        player.maxHealth += self.modifications.get("maxHealthMod")
        player.health += self.modifications.get("healthMod")
        player.damageMultiplier += self.modifications.get("damageMultiplierMod")
        self.player = player
        player.timedPowerups.append(self)
    
    def timerDone(self):
        self.player.maxJumps -= self.modifications.get("maxJumps")
        self.player.jumpSpeed -= self.modifications.get("jumpSpeedMod")
        self.player.speed -= self.modifications.get("speedMod")
        self.player.maxHealth -= self.modifications.get("maxHealthMod")
        self.player.health -= self.modifications.get("healthMod")
        self.player.damageMultiplier -= self.modifications.get("damageMultiplierMod")
        self.player.timedPowerups.remove(self)