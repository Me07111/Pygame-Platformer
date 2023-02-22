from config import healthBarColors,healthBarPoses,healthBarSize,weaponUiPoses,weaponUitextSize
import pygame
class Ui():
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
            if(len(players[i].sprites()) > 1):
                text = f"{players[i].sprites()[1].ammo}"
                font = pygame.font.SysFont("timesnewroman",weaponUitextSize)
                image = pygame.font.Font.render(font,text,False,healthBarColors[i])
                self.screen.blit(image,weaponUiPoses[i])
        
