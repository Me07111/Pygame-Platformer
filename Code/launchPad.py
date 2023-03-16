import pygame
from animator import Animator
from config import scaleRect, scaleValue
class LaunchPad(pygame.sprite.Sprite):
    def __init__(self,pos,jumpPower,height):
        super().__init__()
        self.height = height
        self.idleImage = pygame.image.load("Graphics/JumpPad.png")
        self.launchAnim = pygame.image.load("Graphics/JumpPadLaunch.png")
        self.image = self.idleImage
        self.jumpPower = scaleValue(self.height,jumpPower)
        self.animator = Animator([self.idleImage,self.launchAnim],(40,40),[0.1,0.1])
        self.rect = pygame.Rect(pos,scaleRect(self.height,(40,40)))
        self.rect.center = pos
    def update(self,delta):
        self.image = self.animator.animate(0,delta)
    def onCollision(self,player):
        player.launch((0,1),self.jumpPower)