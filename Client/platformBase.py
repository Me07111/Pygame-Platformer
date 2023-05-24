import pygame
class PlatformBase(pygame.sprite.Sprite):
    def __init__(self,InPos,width : int,height : int,color : int, surface : pygame.Surface):
        super().__init__()
        self.image = pygame.transform.smoothscale(pygame.image.load(f"Graphics/platform{color}.png"),(width,height))
        self.rect = self.image.get_rect()
        self.rect.topleft = InPos