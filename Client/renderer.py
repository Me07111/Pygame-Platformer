import pygame
class Renderer:
    def __init__(self,screen : pygame.Surface) -> None:
        self.screen = screen 
        self.sprites = []
        self.pics = []
        self.rects = []


    def update(self):
        for sprite in self.sprites:
            sprite.draw(self.screen)
        for rect in self.rects:
            pygame.draw.rect(self.screen,rect[0],rect[1])
        for pic in self.pics:
            self.screen.blit(pic[0],pic[1])
        self.sprites = []
        self.pics = []
        self.rects = []
    
    def renderText(self,surface : pygame.surface.Surface,text : str,fontType : str,size : int,color :pygame.Color,pos : tuple,backGroundColor :pygame.Color = None):
        font = pygame.font.SysFont(fontType,size)
        image = pygame.font.Font.render(font,text,False,color,backGroundColor)
        self.pics.append((image,pos))