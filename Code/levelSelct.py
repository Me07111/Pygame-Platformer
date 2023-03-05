from level import Level
from button import Button
from config import scaleValue,scaleRect
class LevelSelect:
    def __init__(self,screen,width,height,clock,playerCount):
        self.screen = screen
        self.levels = [
            Level(screen,width,height,25,clock,playerCount,0),
            Level(screen,width,height,25,clock,playerCount,1),
            Level(screen,width,height,25,clock,playerCount,2),
        ]
        self.buttons = []
        row = 1
        for i in range(len(self.levels)):
            button = Button((scaleValue(height,100) + scaleValue(height,270)*i,scaleValue(height,200)),scaleRect(height,(200,50)),f"Level {i+1}")
            self.buttons.append(button)

    def update(self,delta,gametime,levelHandler):
        for i, button in enumerate(self.buttons):
            if(button.update(self.screen,gametime)):
                levelHandler.setLevel(self.levels[i])