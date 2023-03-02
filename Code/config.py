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
    ["o","o","w2","o","o","o","o","o","o","w1","o","o","P","o","o","o"],
    ["x","x","x","x","x","x","x","x","x","x","x","x","x","x","x","x"]
    ],
    [
    ["o","o","o","o","o","o","o","o","o","o","o","o","o","o","o","o"],
    ["o","o","o","o","o","o","o","o","o","o","o","o","o","o","o","o"],
    ["o","o","o","o","o","o","o","o","o","o","o","o","o","o","o","o"],
    ["o","o","o","o","x","x","o","o","o","o","o","o","o","o","o","o"],
    ["o","o","x","x","x","o","o","o","o","o","o","o","o","o","o","o"],
    ["o","o","o","o","o","o","o","o","o","o","o","o","o","o","o","o"],
    ["o","o","P","o","o","o","o","o","o","o","o","o","o","o","o","o"],
    ["o","o","w0","o","o","o","o","o","o","w4","o","o","P","o","o","o"],
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
    ["o","o","w3","o","o","o","o","o","o","w6","o","o","P","o","o","o"],
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
["pistol","Graphics/pistol.png",600,"Graphics/pistolBullet.png",300,10,10,12,False,
{
    (0,0) : (0,0),
    (0,1) : (0,20),
    (0,-1) : (-10,-15),
    (1,0) : (0,0),
    (1,1) : (0,0),
    (1,-1) : (-10,-20),
    (-1,0) : (-40,0),
    (-1,1) : (-40,0),
    (-1,-1) : (-25,-20)
},
pygame.Vector2(15,-12),
0,1
],
["Assault Rifle","Graphics/ar.png",300,"Graphics/arBullet.png", 600,1,7,30,True,
{
    (0,0) : (0,0),
    (0,1) : (20,0),
    (0,-1) : (0,-25),
    (1,0) : (0,0),
    (1,1) : (5,-10),
    (1,-1) : (-10,-30),
    (-1,0) : (0,0),
    (-1,1) : (-5,-10),
    (-1,-1) : (10,-25)
},
pygame.Vector2(42,0),
0,1
],
["Sniper","Graphics/Sniper.png",800,"Graphics/sniperBullet.png",30,1,30,5,False,
{
    (0,0) : (0,0),
    (0,1) : (0,0),
    (0,-1) : (0,0),
    (1,0) : (0,0),
    (1,1) : (0,0),
    (1,-1) : (0,0),
    (-1,0) : (0,0),
    (-1,1) : (0,0),
    (-1,-1) : (0,0)
},
pygame.Vector2(50,0),
0,1
],
["Shotgun","Graphics/shotgun.png",800,"Graphics/slug.png",200,1,20,6,False,
{
    (0,0) : (0,0),
    (0,1) : (0,0),
    (0,-1) : (0,0),
    (1,0) : (0,0),
    (1,1) : (0,0),
    (1,-1) : (0,0),
    (-1,0) : (0,0),
    (-1,1) : (0,0),
    (-1,-1) : (0,0)
},
pygame.Vector2(40,-10),
5,6
],
["Rpg-7","Graphics/rpg7.png",300,"Graphics/rpg7rocket.png",12,1,50,3,False,
{
    (0,0) : (0,0),
    (0,1) : (0,0),
    (0,-1) : (0,0),
    (1,0) : (0,0),
    (1,1) : (0,0),
    (1,-1) : (0,0),
    (-1,0) : (0,0),
    (-1,1) : (0,0),
    (-1,-1) : (0,0)
},
pygame.Vector2(),
0,1
],
["MCX","Graphics/MCX.png",600,"Graphics/arBullet.png",600,1,6,30,True,
{
    (0,0) : (0,0),
    (0,1) : (0,0),
    (0,-1) : (0,0),
    (1,0) : (0,0),
    (1,1) : (0,0),
    (1,-1) : (0,0),
    (-1,0) : (0,0),
    (-1,1) : (0,0),
    (-1,-1) : (0,0)
},
pygame.Vector2(),
0,1
],
["desert Eagle","Graphics/deagle.png",500,"Graphics/pistolBullet.png",120,4,20,7,False,
{
    (0,0) : (0,0),
    (0,1) : (0,0),
    (0,-1) : (0,0),
    (1,0) : (0,0),
    (1,1) : (0,0),
    (1,-1) : (0,0),
    (-1,0) : (0,0),
    (-1,1) : (0,0),
    (-1,-1) : (0,0)
},
pygame.Vector2(),
0,1
]
]

def renderText(surface,text,fontType,size,color,pos,backGroundColor = None):
    font = pygame.font.SysFont(fontType,size)
    image = pygame.font.Font.render(font,text,False,color,backGroundColor)
    surface.blit(image,pos)