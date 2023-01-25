import pygame
from player import Character
from config import map

class Level:
    def __init__(self,screen,width,height):
        self.screen = screen
        self.PlayerGroup = pygame.sprite.GroupSingle()
        self.width = width
        self.height = height
        self.player1 = Character(pygame.math.Vector2(self.width/2, self.height/2),pygame.Color(255,0,0,255),self.screen,20,50)

    def setup(self):
        self.PlayerGroup.add(self.player1)
    def update(self):
            self.player1.update(pygame.time.get_ticks())
            self.PlayerGroup.draw(self.screen)
