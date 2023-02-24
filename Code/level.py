import pygame
from player import Character
from config import maps,tileWidth,tileHeight,mappings,healthBarPoses,healthBarSize,healthBarColors,weapons
from platformBase import PlatformBase
from weapon import Weapon
from ui import Ui

class Level:
    def __init__(self,screen,width,height,gravity,clock,playercount,map):
        self.screen = screen
        self.clock = clock
        self.ui = Ui(screen)
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
        self.generateMap(map)

    def update(self,delta,gametime,levelHandler):
        keys = pygame.key.get_pressed()
        for i in range(len(self.players)):
            player = self.players[i]
            if(player.isOnGround):
                self.horizontalDrag = self.GroundDrag
            else:
                self.horizontalDrag = self.AirDrag
            self.movementUpdate(delta,keys,player,gametime)
            self.pickupUpdate(player,i)
            self.shootUpdate(player,keys,i,gametime)
            self.lookDirUpdate(i,player,keys)
            self.checkWinCondition(player,levelHandler)
            player.lookInDir()
            self.screen.blit(player.image,player.rect.topleft)
            if(player.weapon != None):
                self.screen.blit(player.weapon.image,player.weapon.rect.topleft)
        for bullet in self.bullets:
            self.bulletUpdate(bullet,delta)
        self.platforms.draw(self.screen)
        self.onGroundWeapons.draw(self.screen)
        self.bullets.draw(self.screen)
        self.ui.update(self.players)

    def checkWinCondition(self,player,levelHandler):
        if(player.health <= 0):
                levelHandler.backToMenu()

    def bulletUpdate(self,bullet,delta):
        bullet.velocity.y += self.gravity * bullet.gravMul * delta
        bullet.rect.center = bullet.rect.center + bullet.velocity * delta
        if(len(pygame.sprite.spritecollide(bullet,self.platforms,False)) > 0):
            self.bullets.remove(bullet)
        for player in self.players:
            if(pygame.sprite.collide_rect(bullet,player) > 0 and player != bullet.ignored):
                player.takeDamage(bullet.damage)
                self.bullets.remove(bullet)

    def lookDirUpdate(self,i,player,keys):
        if(keys[mappings[i][0]]):
            player.lookDir = pygame.Vector2(-1,0)
        elif(keys[mappings[i][1]]):
            player.lookDir = pygame.Vector2(1,0)
        elif(keys[mappings[i][2]]):
            player.lookDir = pygame.Vector2(0,-1)
        elif(keys[mappings[i][3]]):
            player.lookDir = pygame.Vector2(0,1)
        if(keys[mappings[i][0]] and keys[mappings[i][2]]):
            player.lookDir = pygame.Vector2(-1,-1)
        elif(keys[mappings[i][0]] and keys[mappings[i][3]]):
            player.lookDir = pygame.Vector2(-1,1)
        elif(keys[mappings[i][1]] and keys[mappings[i][2]]):
            player.lookDir = pygame.Vector2(1,-1)
        elif(keys[mappings[i][1]] and keys[mappings[i][3]]):
            player.lookDir = pygame.Vector2(1,1)
        
    def shootUpdate(self,player,keys,i,gameTime):
        if(player.weapon != None):
            if(keys[mappings[i][4]]):
                if(pygame.Vector2.length(player.lookDir) > 0):
                   player.weapon.shoot(pygame.Vector2.normalize(player.lookDir),self,gameTime,player)
                else:
                   player.weapon.shoot(pygame.Vector2(1,0),self,gameTime,player)
            else:
               player.weapon.wasShotReleased = True

    def pickupUpdate(self,player,i):
        collidingWeapons = pygame.sprite.spritecollide(player,self.onGroundWeapons,False)
        if(len(collidingWeapons) > 0):
            if(player.weapon != None):
                if(player.weapon.name == collidingWeapons[0].name):
                   player.weapon.ammo +=player.weapon.maxAmmo
                else:
                    player.weapon = None
                    player.weapon = collidingWeapons[0]
            else:
                player.weapon = collidingWeapons[0]
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

    def generateMap(self,mapIndex):
        playerAmount = 0
        map = maps[mapIndex]
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
                    weapon = Weapon(type[0],type[1],False,pos,type[2],type[3],type[4],type[5],type[6],type[7],type[8],type[9],type[10])
                    self.onGroundWeapons.add(weapon)
    
    def closerToZero(self,numberToNegate,negateBy):
        if(numberToNegate >= 0):
            index = 1
        else:
            index = -1
        if((abs(numberToNegate) - negateBy) < 0):
            return 0
        else:
            return (abs(numberToNegate) - negateBy) * index