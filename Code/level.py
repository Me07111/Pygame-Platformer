import pygame
from player import Character
from config import map,tileWidth,tileHeight
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
        self.PlayerGroup.draw(self.screen)
        self.platforms.draw(self.screen)

    def horizontalUpdate(self,delta,keys):
        self.player1.direction.x = 0
        if(keys[pygame.K_a]):
            self.player1.direction.x = -1
        if(keys[pygame.K_d]):
            self.player1.direction.x = 1
        oldPos = self.player1.rect.center
        self.player1.rect.centerx += self.player1.direction.x * self.player1.speed * delta
        collidingPlatforms = pygame.sprite.spritecollide(self.player1,self.platforms,False)
        if(len(collidingPlatforms) > 0):
            self.player1.rect.center = oldPos
            self.player1.direction.x = 0
            


    def verticalUpdate(self,delta,keys):
        if(keys[pygame.K_SPACE]):
            if(self.player1.jumpIndex > 0):
                self.player1.direction.y -= self.player1.jumpSpeed
                self.player1.jumpIndex -= 1
        self.player1.direction.y += (self.player1.direction.y + self.gravity) * delta
        oldPos = self.player1.rect.center
        self.player1.rect.centery += self.player1.direction.y
        collidingPlatforms = pygame.sprite.spritecollide(self.player1,self.platforms,False)
        if(len(collidingPlatforms) > 0):
            self.player1.rect.center = oldPos
            self.player1.direction.y = 0
            self.player1.jumpIndex = self.player1.maxJumps

    def generatePlatforms(self):
        cellHeight = self.height/len(map)
        cellWidth = self.width/len(map[0])
        for i in range(len(map)):
            row = map[i]
            for j in range(len(row)):
                cell = row[j]
                if(cell == "o"):
                    continue
                elif(cell == "x"):
                    pos = pygame.math.Vector2(j*tileWidth,i*tileHeight)
                    print(pos)
                    platform = PlatformBase(pos,cellWidth,cellHeight,pygame.color.Color(255,255,255,255),self.screen)
                    self.platforms.add(platform)
                     


