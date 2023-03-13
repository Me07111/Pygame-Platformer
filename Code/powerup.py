from config import scaleRect
import pygame
from animator import Animator
class PowerUp(pygame.sprite.Sprite):
    def __init__(self,height : int,pos,name : str,imagePath : str,modifications : dict):
        super().__init__()
        self.height = height
        self.origImage = pygame.image.load(imagePath)
        self.image = pygame.transform.smoothscale(self.origImage,scaleRect(height,(40,40)))
        self.rect = self.image.get_rect()
        self.rect.center = pos
        self.modifications = modifications
        self.animator = Animator([self.origImage],(40,40),[1])

    def update(self,delta : float, *args: any, **kwargs: any) -> None:
        super().update(*args, **kwargs)
        self.origImage = self.animator.animate(0,delta)
        self.image = pygame.transform.smoothscale(self.origImage,scaleRect(self.height,(40,40)))
        
    
    def pickUp(self,player):
        player.maxJumps = self.modifications.get("maxJumps")
        player.jumpSpeed += self.modifications.get("jumpSpeedMod")
        player.speed += self.modifications.get("speedMod")
        player.maxHealth += self.modifications.get("maxHealthMod")
        player.health += self.modifications.get("healthMod")
