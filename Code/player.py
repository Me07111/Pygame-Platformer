import pygame
class Character(pygame.sprite.Sprite):
    def __init__(self,InPos,surface,keys):
        super().__init__()
        self.direction = pygame.math.Vector2(0,0)
        self.jumpSpeed = 6
        self.jumpIndex = 1
        self.maxJumps = 2
        self.jumpDelay = 0.35
        self.lastJumpTime = -self.jumpDelay
        self.speed = 200
        self.surface = surface
        self.image = pygame.image.load("Graphics\Character.png")
        self.rect = self.image.get_rect()
        self.rect.center = InPos
        print(self.rect)
        self.leftKey = keys[0]
        self.rightKey = keys[1]
        self.jumpKey = keys[2]
        