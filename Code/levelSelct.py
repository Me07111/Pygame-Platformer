from level import Level
from button import Button
from config import scaleValue,scaleRect
import pygame
import math
from levelEditor import LevelEditor
class LevelSelect:
    def __init__(self,screen,width : float,height : float,clock,playerCount : int):
        self.screen = screen
        self.levels = [
            Level(screen,width,height,25,clock,playerCount,0),
            Level(screen,width,height,25,clock,playerCount,1),
            Level(screen,width,height,25,clock,playerCount,2),
            Level(screen,width,height,25,clock,playerCount,0),
            Level(screen,width,height,25,clock,playerCount,1),
            Level(screen,width,height,25,clock,playerCount,2),
            Level(screen,width,height,25,clock,playerCount,0),
            Level(screen,width,height,25,clock,playerCount,1),
            Level(screen,width,height,25,clock,playerCount,2),
            Level(screen,width,height,25,clock,playerCount,0),
            Level(screen,width,height,25,clock,playerCount,1),
            Level(screen,width,height,25,clock,playerCount,2),
            Level(screen,width,height,25,clock,playerCount,0),
            Level(screen,width,height,25,clock,playerCount,1),
            Level(screen,width,height,25,clock,playerCount,2),
            LevelEditor((32,18),height,screen,-1)
        ]
        self.buttons = []
        for i in range(math.ceil(len(self.levels) / 4)):
            for j in range(4):
                if(len(self.levels) - 1 >= i*4 + j):
                    if(i*4 + j +1 == 16):
                        text = "Level Editor"
                    else:   
                        text = f"Level {i*4 + j +1}"
                    button = Button(scaleRect(height,(200 + 270*j,100 + i * 175)),scaleRect(height,(200,50)),text,pygame.Color(255,255,255),scaleValue(height,20))
                    self.buttons.append(button)

    def update(self,delta : float,gametime : float,levelHandler):
        for i, button in enumerate(self.buttons):
            if(button.update(self.screen,gametime)[0]):
                levelHandler.setLevel(self.levels[i])