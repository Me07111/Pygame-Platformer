import pygame
from player import Character
from config import map,tileWidth,tileHeight,mappings,healthBarPoses,healthBarSize,healthBarColors,weapons
from platformBase import PlatformBase
from weapon import Weapon

class Level:
    def __init__(self,screen,width,height,gravity,clock,playercount):
        self.screen = screen
        self.clock = clock
        self.width = width
        self.height = height
        self.gravity = gravity
        self.platforms = pygame.sprite.Group()
        self.bullets = pygame.sprite.Group()
        self.playerCount = playercount
        self.players = []
        self.horizontalDrag = 0.1
        self.GroundDrag = 0.1
        self.AirDrag = 0.01
        self.onGroundWeapons = pygame.sprite.Group()
        self.generatePlatforms()

    def update(self,delta,gametime):
        keys = pygame.key.get_pressed()
        for i in range(len(self.players)):
            player = self.players[i]
            if(player.isOnGround):
                self.horizontalDrag = self.GroundDrag
            else:
                self.horizontalDrag = self.AirDrag
            self.movementUpdate(delta,keys,player,gametime)
            self.updatePickup(player,i)
            player.setSpritesPos()
            self.shootUpdate(player,keys,i,gametime)
            player.draw(self.screen)
        self.platforms.draw(self.screen)
        self.onGroundWeapons.draw(self.screen)
        self.bullets.draw(self.screen)
        self.displayHealthBars()
    
    def shootUpdate(self,player,keys,i,gameTime):
        if(keys[mappings[i][3]]):
            if(pygame.Vector2.length(player.direction) > 0):
                player.sprites()[1].shoot(pygame.Vector2.normalize(player.direction),self,gameTime)
            else:
                player.sprites()[1].shoot(pygame.Vector2(1,0),self,gameTime)

    def updatePickup(self,player,i):
        collidingWeapons = pygame.sprite.spritecollide(player.sprite,self.onGroundWeapons,False)
        if(len(collidingWeapons) > 0):
            player.add(collidingWeapons[0])
            self.onGroundWeapons.remove(collidingWeapons[0])

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
        oldPos = player.sprite.rect.center
        player.direction.y += (player.direction.y + self.gravity) * delta
        player.sprite.rect.centery += player.direction.y
        collidingPlatformsVert = pygame.sprite.spritecollide(player.sprite,self.platforms,False)
        if(len(collidingPlatformsVert) > 0):
            player.sprite.rect.center = oldPos
            player.direction.y = 0
            player.jumpIndex = player.maxJumps
            player.isOnGround = True

        #horizontal update
        oldPos = player.sprite.rect.center
        player.sprite.rect.centerx += player.direction.x * player.speed * delta
        player.direction.x = self.closerToZero(player.direction.x,self.horizontalDrag)
        collidingPlatforms = pygame.sprite.spritecollide(player.sprite,self.platforms,False)
        if(len(collidingPlatforms) > 0):
            player.sprite.rect.center = oldPos
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
                        playerAmount += 1
                elif(cell[0] == "w"):
                    type = weapons[int(cell[len(cell)-1])]
                    weapon = Weapon(type[0],type[1],False,pos,type[2],type[3],type[4])
                    self.onGroundWeapons.add(weapon)
    
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