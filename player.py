import pygame
class Character:
    def __init__(self,InPos,color,surface,width,height):
        self.pos = InPos
        self.velocity = pygame.Vector2(0,0)
        self.jumpSpeed = 50
        self.gravity = 500
        self.speed = 0.0001
        self.color = color
        self.surface = surface
        self.rect = pygame.Rect(InPos,width,height)
    
    def update(self,delta):
        self.move(delta)
        self.draw()
    def move(self,delta):
        keys = pygame.key.get_pressed()
        self.velocity = pygame.Vector2(0,0)
        if(keys[pygame.K_a]):
            self.velocity.x += -1
        if(keys[pygame.K_d]):
            self.velocity.x += 1
        self.pos += self.velocity * self.speed * delta
    def draw(self):
        pygame.draw.rect(self.surface,self.color,self.rect)