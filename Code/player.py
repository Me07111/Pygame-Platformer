import pygame
from config import renderText
class Character(pygame.sprite.Sprite):
    def __init__(self,InPos,surface,keys,name):
        super().__init__()
        self.direction = pygame.math.Vector2(0,0)
        self.jumpSpeed = 10
        self.maxJumps = 2
        self.jumpIndex = self.maxJumps
        self.jumpDelay = 0.35
        self.lastJumpTime = -self.jumpDelay
        self.speed = 400
        self.surface = surface
        self.origImage = pygame.image.load("Graphics\Character.png")
        self.image = self.origImage
        self.rect = self.image.get_rect()
        print(self.rect)
        self.rect.center = InPos
        self.leftKey = keys[0]
        self.rightKey = keys[1]
        self.jumpKey = keys[2]
        self.maxHealth = 100
        self.health = self.maxHealth
        self.launchVector = pygame.Vector2()
        self.launchSpeed = 0
        self.launched = False
        self.isOnGround = True
        self.lookDir = pygame.Vector2(0,0)
        self.weapon = None
        self.name = name

    def takeDamage(self,damage):
        self.health -= damage
        if(self.health <= 0):
            self.health = 0
            
    def heal(self,healAmount):
        self.health += healAmount
        if(self.health > self.maxHealth):
            self.health = self.maxHealth

    def launch(self,direction,speed):
        print("launched")
        self.launchVector = direction
        self.launchSpeed = speed
        self.launched = True
    
    def lookInDir(self):
        if(self.lookDir.x == -1):
            self.image = pygame.transform.flip(self.origImage,True,False)
        elif(self.lookDir.x == 1):
            self.image = self.origImage
        if(self.weapon != None):
            if(self.lookDir.x == -1):
                self.weapon.isFlipped = True
            else:
                self.weapon.isFlipped = False
            if(self.lookDir.x == 1 and self.lookDir.y == 1):
                self.weapon.image = pygame.transform.rotate(self.weapon.origImage,-45)
                self.weapon.rotation = -45
            elif(self.lookDir.x == -1 and self.lookDir.y == 1):
                self.weapon.image = pygame.transform.rotate(pygame.transform.flip(self.weapon.origImage,True,False),45)
                self.weapon.rotation = -45
            elif(self.lookDir.x == -1 and self.lookDir.y == -1):
                self.weapon.image = pygame.transform.rotate(pygame.transform.flip(self.weapon.origImage,True,False),-45)
                self.weapon.rotation = 45
            elif(self.lookDir.x == 1 and self.lookDir.y == -1):
                self.weapon.image = pygame.transform.rotate(self.weapon.origImage,45)
                self.weapon.rotation = -45
            elif(self.lookDir.x == -1):
                self.weapon.image = pygame.transform.flip(self.weapon.origImage,True,False)
                self.weapon.rotation = 0
            elif(self.lookDir.x == 1):
                self.weapon.image = self.weapon.origImage
                self.weapon.rotation = 0
            elif(self.lookDir.y == -1):
                self.weapon.image = pygame.transform.rotate(self.weapon.origImage,90)
                self.weapon.rotation = -90
            elif(self.lookDir.y == 1):
                self.weapon.image = pygame.transform.rotate(self.weapon.origImage,-90)
                self.weapon.rotation = 90
        if(self.weapon != None):
                lookDir = (self.lookDir.x,self.lookDir.y)
                self.weapon.rect.center = (self.rect.centerx + self.weapon.offsets[lookDir][0],self.rect.centery + self.weapon.offsets[lookDir][1])
                print(self.weapon.rect)

    def draw(self,screen):
        screen.blit(self.image,self.rect.topleft)
        renderText(screen,self.name,"timesnewroman",20,pygame.color.Color(0,0,0),(self.rect.topleft[0],self.rect.topleft[1] - 20))
        if(self.weapon != None):
            screen.blit(self.weapon.image,self.weapon.rect.topleft)