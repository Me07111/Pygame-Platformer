import pygame
class Character(pygame.sprite.Sprite):
    def __init__(self,InPos,surface,keys):
        super().__init__()
        self.direction = pygame.math.Vector2(0,0)
        self.jumpSpeed = 10
        self.maxJumps = 2
        self.jumpIndex = self.maxJumps
        self.jumpDelay = 0.35
        self.lastJumpTime = -self.jumpDelay
        self.speed = 200
        self.surface = surface
        self.image = pygame.image.load("Graphics\Character.png")
        self.rect = self.image.get_rect()
        self.rect.center = InPos
        self.leftKey = keys[0]
        self.rightKey = keys[1]
        self.jumpKey = keys[2]
        self.maxHealth = 100
        self.health = self.maxHealth
        self.launchVector = pygame.Vector2()
    
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
        self.launchVector += direction * speed
