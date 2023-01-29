import pygame
class Character(pygame.sprite.Sprite):
    def __init__(self,InPos,color,surface,width,height):
        super().__init__()
        self.pos = InPos
        self.direction = pygame.math.Vector2(0,0)
        self.jumpSpeed = 0.01
        self.jumpIndex = 1
        self.gravity = 500
        self.speed = 0.01
        self.color = color
        self.surface = surface
        self.image = pygame.image.load("Graphics\Character.png")
        self.rect = self.image.get_rect()
        self.rect.center = self.pos
        print(self.rect)
        