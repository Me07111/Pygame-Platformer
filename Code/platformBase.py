import pygame
class PlatformBase(pygame.sprite.Sprite):
    def __init__(self,InPos,width,height,color,surface):
        super().__init__()
        self.color = color
        self.image = pygame.image.load("Graphics/Platform.png")
        self.rect = self.image.get_rect()
        self.rect.topleft = InPos