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
        self.crap = True

    def update(self,delta,gametime):
        if(gametime > 3 and self.crap):
            self.players[1].launch(pygame.Vector2(1,1),6)
        keys = pygame.key.get_pressed()
        for player in self.players:
            self.movementUpdate(delta,keys,player,gametime)
        self.PlayerGroup.draw(self.screen)
        self.platforms.draw(self.screen)
        self.displayHealthBars()

    def movementUpdate(self,delta,keys,player,gameTime):
        #input
        player.direction.x = 0
        if(keys[player.leftKey]):
            player.direction.x = -1
        if(keys[player.rightKey]):
            player.direction.x = 1
        if(keys[player.jumpKey]):
            if(player.jumpIndex > 0 and abs(gameTime-player.lastJumpTime) > player.jumpDelay):
                player.direction.y = 0
                player.direction.y -= player.jumpSpeed
                player.jumpIndex -= 1
                player.lastJumpTime = gameTime

        #vertical update
        oldPos = player.rect.center
        player.direction.y += (player.direction.y + self.gravity) * delta
        player.rect.centery += player.direction.y
        collidingPlatformsVert = pygame.sprite.spritecollide(player,self.platforms,False)
        if(len(collidingPlatformsVert) > 0):
            player.rect.center = oldPos
            player.direction.y = 0
            player.jumpIndex = player.maxJumps

        #horizontal update
        player.rect.centerx += player.direction.x * player.speed * delta
        collidingPlatforms = pygame.sprite.spritecollide(player,self.platforms,False)
        if(len(collidingPlatforms) > 0):
            player.rect.center = oldPos
            player.direction.x = 0
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
            rect = pygame.Rect(
            healthBarPoses[i].x,
            healthBarPoses[i].y,
            healthBarSize.x*(self.players[i].health/self.players[i].maxHealth),
            healthBarSize.y
            )
            pygame.draw.rect(self.screen,healthBarColors[i],rect)