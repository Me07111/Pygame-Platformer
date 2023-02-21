import pygame
class Character(pygame.sprite.Group):
    def __init__(self,InPos,surface,keys):
        super().__init__()
        self.direction = pygame.math.Vector2(0,0)
        self.jumpSpeed = 10
        self.maxJumps = 2
        self.jumpIndex = self.maxJumps
        self.jumpDelay = 0.35
        self.lastJumpTime = -self.jumpDelay
        self.speed = 400
        self.surface = surface
        self.sprite = pygame.sprite.Sprite()
        self.origImage = pygame.image.load("Graphics\Character.png")
        self.sprite.image = self.origImage
        self.sprite.rect = self.sprite.image.get_rect()
        self.sprite.rect.center = InPos
        self.add(self.sprite)
        self.leftKey = keys[0]
        self.rightKey = keys[1]
        self.jumpKey = keys[2]
        self.maxHealth = 100
        self.health = self.maxHealth
        self.launchVector = pygame.Vector2()
        self.launchSpeed = 0
        self.launched = False
        self.isOnGround = True
        self.weapon = None
        self.lookDir = pygame.Vector2(0,0)
    
    def takeDamage(self,damage):
        self.health -= damage
        if(self.health <= 0):
            self.health = 0
            self.die()
            
    def heal(self,healAmount):
        self.health += healAmount
        if(self.health > self.maxHealth):
            self.health = self.maxHealth

    def die(self):
        print("dead")      

    def launch(self,direction,speed):
        print("launched")
        self.launchVector = direction
        self.launchSpeed = speed
        self.launched = True

    def setSpritesPos(self):
        for sprite in self.sprites():
            sprite.rect.center = self.sprite.rect.center
    
    def lookInDir(self):
        if(self.lookDir.x == -1):
            self.sprites()[0].image = pygame.transform.flip(self.origImage,True,False)
        elif(self.lookDir.x == 1):
            self.sprites()[0].image = self.origImage
        if(len(self.sprites()) >= 2):
            if(self.lookDir.x == 1 and self.lookDir.y == 1):
                self.sprites()[1].image = pygame.transform.rotate(self.sprites()[1].origImage,45)
            elif(self.lookDir.x == -1 and self.lookDir.y == 1):
                self.sprites()[1].image = pygame.transform.rotate(pygame.transform.flip(self.sprites()[1].origImage,True,False),45)
            elif(self.lookDir.x == -1 and self.lookDir.y == -1):
                self.sprites()[1].image = pygame.transform.rotate(pygame.transform.flip(self.sprites()[1].origImage,True,False),-45)
            elif(self.lookDir.x == 1 and self.lookDir.y == -1):
                self.sprites()[1].image = pygame.transform.rotate(self.sprites()[1].origImage,-45)
            elif(self.lookDir.x == -1):
                self.sprites()[1].image = pygame.transform.flip(self.sprites()[1].origImage,True,False)
            elif(self.lookDir.x == 1):
                self.sprites()[1].image = self.sprites()[1].origImage
            elif(self.lookDir.y == -1):
                self.sprites()[1].image = pygame.transform.rotate(self.sprites()[1].origImage,90)
            elif(self.lookDir.y == 1):
                self.sprites()[1].image = pygame.transform.rotate(self.sprites()[1].origImage,-90)
            
        