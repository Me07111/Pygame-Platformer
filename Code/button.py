import pygame
class Button(pygame.sprite.Sprite):
    def __init__(self,pos,size,method,hoveredTint,path):
        super().__init__()
        self.image = pygame.transform.scale(pygame.image.load(path),size)
        self.rect = self.image.get_rect()
        self.rect.center = pos
        self.hoveredTint = hoveredTint
        self.method = method
    
    def update(self,screen):
        mousePos = pygame.mouse.get_pos()
        if(pygame.Rect.collidepoint(self.rect,mousePos[0],mousePos[1])):
            if(pygame.mouse.get_pressed(3)[0]):
                self.method()
            else:
                screen.blit(self.image.fill(self.hoveredTint),self.rect.topleft)