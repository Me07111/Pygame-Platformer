import pygame
from player import Character
from config import map

class Level:
    def __init__(self,screen,width,height,gravity):
        self.screen = screen
        self.PlayerGroup = pygame.sprite.GroupSingle()
        self.width = width
        self.height = height
        self.player1 = Character(pygame.math.Vector2(self.width/2, self.height/2),pygame.Color(255,0,0,255),self.screen,20,50)
        self.gravity = gravity

    def setup(self):
        self.PlayerGroup.add(self.player1)
    def update(self):
            keys = pygame.key.get_pressed()
            delta = pygame.time.get_ticks()
            self.horizontalUpdate(delta,keys)
            self.verticalUpdate(delta,keys)
            self.player1.rect.center = self.player1.pos
            self.PlayerGroup.draw(self.screen)
            print(self.player1.rect.center,keys[pygame.K_SPACE])
    def horizontalUpdate(self,delta,keys):
        self.player1.direction.x = 0
        if(keys[pygame.K_a]):
            self.player1.direction.x = -1
        if(keys[pygame.K_d]):
            self.player1.direction.x = 1
        self.player1.pos.x += self.player1.direction.x * self.player1.speed * delta
    def verticalUpdate(self,delta,keys):
            if(keys[pygame.K_SPACE]):
                if(self.player1.jumpIndex > 0):
                    self.player1.direction.y -= self.player1.jumpSpeed
                    self.player1.jumpIndex -= 1
            self.player1.direction.y += (self.player1.direction.y + self.gravity) * delta
            self.player1.pos.y += self.player1.direction.y          
