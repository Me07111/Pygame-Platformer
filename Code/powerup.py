from config import scaleRect
import pygame
class PowerUp(pygame.sprite.Sprite):
    def __init__(self,height : int,pos,name : str,imagePath : str,modifications : dict):
        super().__init__()
        self.height = height
        self.origImage = pygame.image.load(imagePath)
        self.image = pygame.transform.scale(self.origImage,scaleRect(height,self.origImage.get_width(),self.origImage.get_height()))
        self.rect = self.image.get_rect()
        self.rect.center = pos
        self.modifications = modifications
    
    def pickUp(self,player):
        player.maxJumps = self.modifications.get("maxJumps")
        player.jumpSpeed += self.modifications.get("jumpSpeedMod")
        player.speed += self.modifications.get("speedMod")
        player.maxHealth += self.modifications.get("maxHealthMod")
        player.health += self.modifications.get("healthMod")
