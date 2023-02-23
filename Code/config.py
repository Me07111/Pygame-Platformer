import pygame
maps = [
    [
    ["o","o","o","o","o","o","o","o","o","o","o","o","o","o","o","o"],
    ["o","o","o","o","o","o","o","o","o","o","o","o","o","o","o","o"],
    ["o","o","o","o","o","o","o","o","o","o","o","o","o","o","o","o"],
    ["o","o","o","o","P","o","o","o","o","o","o","o","o","o","o","o"],
    ["o","o","o","o","o","o","o","o","o","o","o","o","o","o","o","o"],
    ["o","o","o","o","o","o","o","o","o","o","o","o","o","o","o","o"],
    ["o","o","o","o","o","o","o","o","o","o","o","o","o","o","o","o"],
    ["o","o","w0","o","o","o","o","o","o","w1","o","o","P","o","o","o"],
    ["x","x","x","x","x","x","x","x","x","x","x","x","x","x","x","x"]
    ],
    [
    ["o","o","o","o","o","o","o","o","o","o","o","o","o","o","o","o"],
    ["o","o","o","o","o","o","o","o","o","o","o","o","o","o","o","o"],
    ["o","o","o","o","o","o","o","o","o","o","o","o","o","o","o","o"],
    ["o","o","o","o","P","x","o","o","o","o","o","o","o","o","o","o"],
    ["o","o","x","x","x","o","o","o","o","o","o","o","o","o","o","o"],
    ["o","o","o","o","o","o","o","o","o","o","o","o","o","o","o","o"],
    ["o","o","o","o","o","o","o","o","o","o","o","o","o","o","o","o"],
    ["o","o","w0","o","o","o","o","o","o","w1","o","o","P","o","o","o"],
    ["x","x","x","x","x","x","x","x","x","x","x","x","x","x","x","x"]
    ]
]


tileWidth = 80
tileHeight = 80

player1Mappings = [
pygame.K_a,
pygame.K_d,
pygame.K_w,
pygame.K_s,
pygame.K_SPACE
]

player2Mappings = [
pygame.K_LEFT,
pygame.K_RIGHT,
pygame.K_UP,
pygame.K_DOWN,
pygame.K_BACKSPACE
]

mappings = [
    player1Mappings,
    player2Mappings,
    player1Mappings,
    player2Mappings
]

healthBarSize = pygame.math.Vector2(300,40)

healthBarPoses = [
    pygame.math.Vector2(40,40),
    pygame.math.Vector2(940,40),
    pygame.math.Vector2(40,120),
    pygame.math.Vector2(940,120)
]

weaponUiPoses= [
    pygame.math.Vector2(40 + healthBarSize.x + 10 ,40),
    pygame.math.Vector2(840,40),
    pygame.math.Vector2(40 + healthBarSize.x + 10 ,120),
    pygame.math.Vector2(840,120)
]

weaponUitextSize = int(healthBarSize.y)

uiFontType = "timesnewroman"

healthBarColors = [
    pygame.color.Color(0,255,0,255),
    pygame.color.Color(0,0,255,255),
    pygame.color.Color(255,0,0,255),
    pygame.color.Color(255,100,15,255)
]

#(name,imagePath,isPickedUp,inPos,bulletSpeed,bulletSize,bulletImagePath,fireRate,bulletRelGrav,damage,maxAmmo)
weapons = [
["pistol","Graphics/pistol.png",600,"Graphics/pistolBullet.png",300,10,10,12,False],
["Assault Rifle","Graphics/ar.png",300,"Graphics/arBullet.png", 600,1,7,30,True]
]

def renderText(surface,text,fontType,size,color,pos,backGroundColor = None):
    font = pygame.font.SysFont(fontType,size)
    image = pygame.font.Font.render(font,text,False,color,backGroundColor)
    surface.blit(image,pos)