from level import Level
from button import Button
class LevelSelect:
    def __init__(self,screen,width,height,clock,playerCount):
        self.screen = screen
        self.levels = [
            Level(screen,width,height,25,clock,playerCount,0),
            Level(screen,width,height,25,clock,playerCount,1)
        ]
        self.buttons = []
        for i in range(len(self.levels)):
            button = Button((100 + 270*i,200),(200,50),f"Level {i}")
            self.buttons.append(button)

    def update(self,delta,gametime,levelHandler):
        for i in range(len(self.buttons)):
            button = self.buttons[i]
            if(button.update(self.screen)):
                levelHandler.setLevel(Level)