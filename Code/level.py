import pygame
from player import Character
from config import map
from platformBase import PlatformBase

class Level:
    def __init__(self,screen,width,height,gravity):
        self.screen = screen
        self.PlayerGroup = pygame.sprite.GroupSingle()
        self.width = width
        self.height = height
        self.player1 = Character(pygame.math.Vector2(self.width/2, self.height/2),pygame.Color(255,0,0,255),self.screen,20,50)
        self.gravity = gravity
        self.platforms = pygame.sprite.Group()

    def setup(self):
        self.PlayerGroup.add(self.player1)
        self.generatePlatforms()

    def update(self,delta):
        keys = pygame.key.get_pressed()
        self.horizontalUpdate(delta,keys)
        self.verticalUpdate(delta,keys)
        self.player1.rect.center = self.player1.pos
        self.PlayerGroup.draw(self.screen)
        self.platforms.draw(self.screen)

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

    def generatePlatforms(self):
        cellHeight = self.height/len(map)
        cellWidth = self.width/len(map[0])
        for i, row in map:
            for j, cell in row:
                if(cell == "o"):
                    continue
                elif(cell == "x"):
                    pos = pygame.math.Vector2(self.width/j,self.height/i)
                    platform = PlatformBase(pos,cellWidth,cellHeight,pygame.color.Color(255,255,255,255))
                    self.platforms.add(platform)
                     


