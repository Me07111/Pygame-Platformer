import pygame
from player import Character
from config import mappings,weapons,scaleValue, powerUps,renderer
from platformBase import PlatformBase
from weapon import Weapon
from ui import Ui
from powerup import PowerUp
from launchPad import LaunchPad

class Level:
    def __init__(self,screen : pygame.Surface ,width : int,height : int,gravity : float,clock : pygame.time.Clock,playercount : int,map : int, saveHandler):
        self.screen = screen
        self.clock = clock
        self.ui = Ui(screen)
        self.width = width
        self.height = height
        self.gravity = scaleValue(height,gravity) 
        self.platforms = pygame.sprite.Group()
        self.bullets = pygame.sprite.Group()
        self.playerCount = playercount
        self.players = []
        self.horizontalDrag = 0.1
        self.GroundDrag = 0.1
        self.AirDrag = 0.01
        self.onGroundWeapons = pygame.sprite.Group()
        self.powerups = pygame.sprite.Group()
        self.launchPads = pygame.sprite.Group()
        self.saveHandler = saveHandler
        self.generateMap(map)

    def update(self,delta : float,gametime : float,levelHandler):
        keys = pygame.key.get_pressed()
        for i, player in enumerate(self.players):
            if(player.health == 0):
                continue
            if(player.isOnGround):
                self.horizontalDrag = self.GroundDrag
            else:
                self.horizontalDrag = self.AirDrag
            self.movementUpdate(delta,keys,player,gametime)
            self.pickupUpdate(player,i)
            self.shootUpdate(player,keys,i,gametime)
            self.lookDirUpdate(i,player,keys)
            for powerUp in player.timedPowerups:
                powerUp.update(delta)
            self.updateLaunchPadColls(player)
            player.animate(delta)
            player.lookInDir()
            renderer.sprites.append(player)
        for bullet in self.bullets:
            self.bulletUpdate(bullet,delta)
        for powerUp in self.powerups.sprites():
            powerUp.update(delta)
        self.launchPads.update(delta)
        renderer.sprites.append(self.launchPads)
        renderer.sprites.append(self.platforms)
        renderer.sprites.append(self.onGroundWeapons)
        renderer.sprites.append(self.powerups)
        renderer.sprites.append(self.bullets)
        self.ui.update(self.players)
        self.checkWinCondition(player,levelHandler)

    def updateLaunchPadColls(self,player):
        collidingPads = pygame.sprite.spritecollide(player,self.launchPads,False)
        if(len(collidingPads) > 0):
            collidingPads[0].onCollision(player)

    def checkWinCondition(self,player,levelHandler):
        alivePlayers = []
        for player in self.players:
            if(player.health > 0):
                alivePlayers.append(player)
        if(len(alivePlayers) <= 1 ):
            levelHandler.backToMenu(alivePlayers[0].name)

    def bulletUpdate(self,bullet,delta : float):
        bullet.velocity.y += self.gravity * bullet.gravMul * delta
        bullet.rect.center = bullet.rect.center + bullet.velocity * delta
        if(len(pygame.sprite.spritecollide(bullet,self.platforms,False)) > 0):
            self.bullets.remove(bullet)
        for player in self.players:
            if(pygame.sprite.collide_rect(bullet,player) > 0 and player != bullet.ignored):
                player.takeDamage(bullet.damage * bullet.ignored.damageMultiplier)
                self.bullets.remove(bullet)
        bullet.updateRot()

    def lookDirUpdate(self,i : int,player,keys):
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
        
    def shootUpdate(self,player,keys,i : int,gameTime : float):
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
        collidingPowerUps = pygame.sprite.spritecollide(player,self.powerups,False)
        if(len(collidingPowerUps) > 0):
            collidingPowerUps[0].pickUp(player)
            self.powerups.remove(collidingPowerUps[0])

    def movementUpdate(self,delta : float,keys,player,gameTime : float):
        #input
        if(keys[player.leftKey]):
            player.direction.x = -1
        if(keys[player.rightKey]):
            player.direction.x = 1
        if(keys[player.jumpKey]):
            if(player.jumpIndex > 0 and abs(gameTime-player.lastJumpTime) > player.jumpDelay):
                player.direction.y = -0.1
                player.direction.y -= player.jumpSpeed
                player.jumpIndex -= 1
                player.lastJumpTime = gameTime
        #launch update
        if(player.launched == True):
            player.direction.y = player.launchVector.y * player.launchSpeed * delta
            player.launched = False

        #vertical update
        oldPos = player.rect.center
        player.direction.y += (player.direction.y + self.gravity) * delta
        player.rect.centery += player.direction.y
        collidingPlatformsVert = pygame.sprite.spritecollide(player,self.platforms,False)
        if(len(collidingPlatformsVert) > 0):
            player.rect.center = oldPos
            player.direction.y = 0

        #horizontal update
        oldPos = player.rect.center
        player.rect.centerx += player.direction.x * player.speed * delta
        player.direction.x = self.closerToZero(player.direction.x,self.horizontalDrag)
        collidingPlatforms = pygame.sprite.spritecollide(player,self.platforms,False)
        if(len(collidingPlatforms) > 0):
            player.rect.center = oldPos
            player.direction.x = 0
        
        rect = pygame.Rect(player.rect.bottomleft,(player.rect.width,3))
        index = rect.collidelist(self.platforms.sprites())
        if(index != -1):
            player.isOnGround = True
            player.jumpIndex = player.maxJumps
        else:
            player.isOnGround = False

    def generateMap(self,mapIndex : int):
        playerAmount = 0
        map = self.saveHandler.loadMap(mapIndex)
        cellHeight = self.height/len(map)
        cellWidth = self.width/len(map[0])
        playerposes = []
        for i, row in enumerate(map):
            for j, cell in enumerate(row):
                pos = pygame.math.Vector2(j*cellWidth,i*cellHeight)
                if(cell == "o"):
                    continue
                elif(cell == "x"):
                    platform = PlatformBase(pos,cellWidth,cellHeight,pygame.color.Color(255,255,255,255),self.screen)
                    self.platforms.add(platform)
                elif(cell == "P"):
                    if(playerAmount + 1 <= self.playerCount):
                        playerPos = pygame.math.Vector2(pos.x + cellWidth/2,pos.y + cellHeight/2)
                        playerposes.append(playerPos)
                        playerAmount += 1
                elif(cell[0] == "w"):
                    type = weapons[int(cell[len(cell)-1])]
                    weaponPos = pygame.math.Vector2(pos.x + cellWidth/2,pos.y + cellHeight/2)
                    weapon = Weapon(type[0],type[1],False,weaponPos,type[2],type[3],type[4],type[5],type[6],type[7],type[8],type[9],type[10],type[11],type[12],type[13],self.height)
                    self.onGroundWeapons.add(weapon)
                elif(cell[0] == "u"):
                    type = powerUps[int(cell[1])]
                    powerUpPos = (pos.x + cellWidth/2,pos.y + cellHeight/2)
                    powerUp = PowerUp(self.height, powerUpPos, type.get("name"),type.get("imagePath"),type.get("modifications"),type.get("isTimed"),type.get("time"))
                    self.powerups.add(powerUp)
                elif(cell[0] == "L"):
                    print(int(cell[1:len(cell)-1]))
                    launchPad = LaunchPad((pos.x + cellWidth/2,pos.y + cellHeight/2),int(cell[1:len(cell)]),5,self.height)
                    self.launchPads.add(launchPad)
        playerposes.sort(key=getX)
        for i, player in enumerate(playerposes):
            self.players.append(Character(player,self.screen,mappings[i],f"Player {i + 1}",self.height))
    
    def closerToZero(self,numberToNegate : float,negateBy : float):
        if(numberToNegate >= 0):
            index = 1
        else:
            index = -1
        if((abs(numberToNegate) - negateBy) < 0):
            return 0
        else:
            return (abs(numberToNegate) - negateBy) * index
    
def getX(vect : pygame.Vector2) -> int:
    return vect.x