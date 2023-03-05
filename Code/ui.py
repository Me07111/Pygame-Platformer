from config import healthBarColors,healthBarPoses,healthBarSize,weaponUiPoses,weaponUitextSize,uiFontType,renderText
import pygame
class Ui:
    def __init__(self,screen):
        self.screen = screen

    def update(self,players):
        playerCount = len(players)
        for i in range(playerCount):
            rect = pygame.Rect(
            healthBarPoses[i].x,
            healthBarPoses[i].y,
            healthBarSize.x*(players[i].health/players[i].maxHealth),
            healthBarSize.y
            )
            pygame.draw.rect(self.screen,healthBarColors[i],rect)
            if(players[i].weapon != None):
                text = f"{players[i].weapon.ammo}"
                renderText(self.screen,text,uiFontType,weaponUitextSize,healthBarColors[i],weaponUiPoses[i])
        
