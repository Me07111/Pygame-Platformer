from config import scaleRect, clip, healthBarColors,powerUps,healthBarPoses,healthBarSize,weaponUiPoses,weaponUitextSize,uiFontType,renderer,powerUpUiPoses
from animator import Animator
import pygame
class Ui:
    def __init__(self,screen):
        self.screen = screen
        self.height = screen.get_size()[1]
        self.powerUpPics = []
        for powerup in powerUps:
            pic = pygame.transform.smoothscale(clip(pygame.image.load(powerup.get("imagePath")),0,0,40,40),scaleRect(self.height,(30,30)))
            self.powerUpPics.append(pic)

    def update(self,players):
        playerCount = len(players)
        for i in range(playerCount):
            rect = pygame.Rect(
            healthBarPoses[i].x,
            healthBarPoses[i].y,
            healthBarSize.x*(players[i].health/players[i].maxHealth),
            healthBarSize.y
            )
            renderer.rects.append((healthBarColors[i],rect))
            if(players[i].weapon != None):
                text = f"{players[i].weapon.ammo}"
                renderer.renderText(self.screen,text,uiFontType,weaponUitextSize,healthBarColors[i],weaponUiPoses[i])
            timedIndexes = []
            for j, id in enumerate(players[i].activeEffects):
                if(powerUps[id].get("isTimed")):
                    timedIndexes.append(j)
                rect = pygame.rect.Rect((powerUpUiPoses[i].x + 40 * j,powerUpUiPoses[i].y),scaleRect(self.height,(30,30)))
                pic = self.powerUpPics[id]
                renderer.pics.append((pic,rect))
            for j, powerUp in enumerate(players[i].timedPowerups):
                renderer.renderText(self.screen,str("%.2f" % float(powerUp.time-powerUp.timeSincePickUp)),"timesnewroman",18,pygame.Color(255,255,255),((powerUpUiPoses[i].x + 40 * timedIndexes[j],powerUpUiPoses[i].y + 10)))
