import pygame
class PlatformBase(pygame.sprite.Sprite):
    def __init__(self,InPos,width,height,color,surface):
        super().__init__()
        self.color = color
        self.image = pygame.transform.scale(pygame.image.load("Graphics/Platform.png"),(width,height))
        self.rect = self.image.get_rect()
        self.rect.topleft = InPos