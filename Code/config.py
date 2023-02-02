import pygame
map = [
    ["x","o","o","o","o","o","o","o","o","o","o","o","o","o","o","o"],
    ["o","o","o","o","o","o","o","o","o","o","o","o","o","o","o","o"],
    ["o","o","o","o","o","o","o","o","o","o","o","o","o","o","o","o"],
    ["o","o","o","o","P","o","o","o","o","o","o","o","o","o","o","o"],
    ["o","o","o","o","o","o","o","o","o","o","o","o","o","o","o","o"],
    ["o","o","o","o","o","o","o","o","o","o","o","o","o","o","o","o"],
    ["o","o","o","o","o","o","o","o","o","o","o","o","o","o","o","o"],
    ["o","o","o","o","o","o","o","o","o","o","o","o","P","o","o","o"],
    ["x","x","x","x","x","x","x","x","x","x","x","x","x","x","x","x"]
]

tileWidth = 80
tileHeight = 80

player1Mappings = [
pygame.K_a,
pygame.K_d,
pygame.K_SPACE
]

player2Mappings = [
pygame.K_LEFT,
pygame.K_RIGHT,
pygame.K_UP
]

mappings = [
    player1Mappings,
    player2Mappings
]

playerSize = pygame.math.Vector2(100,100)