import pygame
class Character(pygame.sprite.Sprite):
    def __init__(self,InPos,color,surface,width,height):
        super().__init__()
        self.pos = InPos
        self.direction = pygame.math.Vector2(0,0)
        self.jumpSpeed = 50
        self.gravity = 500
        self.speed = 0.0001
        self.color = color
        self.surface = surface
        self.image = pygame.image.load("../Graphics/Character.png")
        self.rect = self.image.get_rect()
        self.rect.center = self.pos
        print(self.rect)
    
    def update(self,delta):
        self.move(delta)
    def move(self,delta):
        self.direction.x = 0
        keys = pygame.key.get_pressed()
        if(keys[pygame.K_a]):
            self.direction.x = -1
        if(keys[pygame.K_d]):
            self.direction.x = 1
        self.pos += self.direction * self.speed * delta
        self.rect.center = self.pos