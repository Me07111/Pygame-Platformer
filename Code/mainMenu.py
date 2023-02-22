import pygame
from button import Button
class MainMenu():
    def __init__(self,screen):
        self.buttons = [
            Button((200,200),(200,50),pygame.quit,pygame.color.Color(0,0,0,0),"Graphics/button.png")
        ]
        self.screen = screen
    
    def update(self):
        for button in self.buttons:
            button.update(self.screen)
