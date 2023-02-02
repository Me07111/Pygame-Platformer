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

healthBarSize = pygame.math.Vector2(300,40)

healthBarPoses = [
    pygame.math.Vector2(40,40),
    pygame.math.Vector2(940,40),
    pygame.math.Vector2(40,240),
    pygame.math.Vector2(940,240)
]

healthBarColors = [
    pygame.color.Color(0,255,0,255),
    pygame.color.Color(0,0,255,255),
    pygame.color.Color(255,0,0,255),
    pygame.color.Color(255,100,15,255)
]