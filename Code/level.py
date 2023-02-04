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
        self.horizontalDrag = 0.1
        self.GroundDrag = 0.1
        self.AirDrag = 0.01

    def update(self,delta,gametime):
        if(gametime > 1 and self.crap == True):
            self.players[1].launch(pygame.Vector2(-1,-4),100)
            self.crap = False
        keys = pygame.key.get_pressed()
        for player in self.players:
            if(player.isOnGround):
                self.horizontalDrag = self.GroundDrag
            else:
                self.horizontalDrag = self.AirDrag
            self.movementUpdate(delta,keys,player,gametime)
        self.PlayerGroup.draw(self.screen)
        self.platforms.draw(self.screen)
        self.displayHealthBars()

    def movementUpdate(self,delta,keys,player,gameTime):
        #input
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
                player.isOnGround = False
        #launch update
        if(player.launched == True):
            player.isOnGround = False
            player.direction += player.launchVector * player.launchSpeed * delta
            player.launched = False

        #vertical update
        oldPos = player.rect.center
        player.direction.y += (player.direction.y + self.gravity) * delta
        player.rect.centery += player.direction.y
        collidingPlatformsVert = pygame.sprite.spritecollide(player,self.platforms,False)
        if(len(collidingPlatformsVert) > 0):
            player.rect.center = oldPos
            player.direction.y = 0
            player.jumpIndex = player.maxJumps
            player.isOnGround = True

        #horizontal update
        oldPos = player.rect.center
        player.rect.centerx += player.direction.x * player.speed * delta
        player.direction.x = self.closerToZero(player.direction.x,self.horizontalDrag)
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
    
    def closerToZero(self,numberToNegate,negateBy):
        if(numberToNegate >= 0):
            index = 1
        else:
            index = -1
        if((abs(numberToNegate) - negateBy) < 0):
            return 0
        else:
            return (abs(numberToNegate) - negateBy) * index