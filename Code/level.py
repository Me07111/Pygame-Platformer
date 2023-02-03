import pygame
from player import Character
from config import map,tileWidth,tileHeight,mappings,healthBarPoses,healthBarSize,healthBarColors
from platformBase import PlatformBase

class Level:
    def __init__(self,screen,width,height,gravity,clock,playercount):
        self.screen = screen
        self.clock = clock
        self.PlayerGroup = pygame.sprite.Group()
        self.width = width
        self.height = height
        self.gravity = gravity
        self.platforms = pygame.sprite.Group()
        self.playerCount = playercount
        self.players = []
        self.generatePlatforms()

    def update(self,delta,gametime):
        keys = pygame.key.get_pressed()
        for player in self.players:
            self.horizontalUpdate(delta,keys,player)
            self.verticalUpdate(delta,keys,gametime,player)
        self.PlayerGroup.draw(self.screen)
        self.platforms.draw(self.screen)
        self.players[0].takeDamage(1)
        self.displayHealthBars()

    def horizontalUpdate(self,delta,keys,player):
        player.direction.x = 0
        if(keys[player.leftKey]):
            player.direction.x = -1
        if(keys[player.rightKey]):
            player.direction.x = 1
        oldPos = player.rect.center
        player.rect.centerx += player.direction.x * player.speed * delta
        collidingPlatforms = pygame.sprite.spritecollide(player,self.platforms,False)
        if(len(collidingPlatforms) > 0):
            player.rect.center = oldPos
            player.direction.x = 0
            player.jumpIndex = player.maxJumps
            


    def verticalUpdate(self,delta,keys,gameTime,player):
        if(keys[player.jumpKey]):
            if(player.jumpIndex > 0 and abs(gameTime-player.lastJumpTime) > player.jumpDelay):
                player.direction.y = 0
                player.direction.y -= player.jumpSpeed
                player.jumpIndex -= 1
                player.lastJumpTime = gameTime

        player.direction.y += (player.direction.y + self.gravity) * delta
        oldPos = player.rect.center
        player.rect.centery += player.direction.y
        collidingPlatforms = pygame.sprite.spritecollide(player,self.platforms,False)
        if(len(collidingPlatforms) > 0):
            player.rect.center = oldPos
            player.direction.y = 0
            player.jumpIndex = player.maxJumps

    def generatePlatforms(self):
        playerAmount = 0
        cellHeight = self.height/len(map)
        cellWidth = self.width/len(map[0])
        for i in range(len(map)):
            row = map[i]
            for j in range(len(row)):
                cell = row[j]
                pos = pygame.math.Vector2(j*tileWidth,i*tileHeight)
                if(cell == "o"):
                    continue
                elif(cell == "x"):
                    platform = PlatformBase(pos,cellWidth,cellHeight,pygame.color.Color(255,255,255,255),self.screen)
                    self.platforms.add(platform)
                elif(cell == "P"):
                    if(playerAmount + 1 <= self.playerCount):
                        playerPos = pygame.math.Vector2(pos.x + 40,pos.y + 40)
                        player = Character(playerPos,self.screen,mappings[playerAmount])
                        self.players.append(player)
                        self.PlayerGroup.add(player)
                        playerAmount += 1
    
    def displayHealthBars(self):
        for i in range(self.playerCount):
            print(self.players[i].health)
            rect = pygame.Rect(
            healthBarPoses[i].x,
            healthBarPoses[i].y,
            healthBarSize.x*(self.players[i].health/self.players[i].maxHealth),
            healthBarSize.y
            )
            pygame.draw.rect(self.screen,healthBarColors[i],rect)