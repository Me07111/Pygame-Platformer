import pygame
from renderer import Renderer
renderer = Renderer(None)

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

spriteSheetPaths = ["Graphics/Character.png","Graphics/PlayerRunningSpriteSheet.png","Graphics/playerJumpAnim.png","Graphics/playerAirAnim.png"]

healthBarSize = pygame.math.Vector2(300,40)

healthBarPoses = [
    pygame.math.Vector2(40,40),
    pygame.math.Vector2(940,40),
    pygame.math.Vector2(40,120),
    pygame.math.Vector2(940,120)
]

powerUpUiPoses = [
    pygame.math.Vector2(40,80),
    pygame.math.Vector2(940,80),
    pygame.math.Vector2(40,160),
    pygame.math.Vector2(940,160)
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

#(name,imagePath,bulletSpeed,bulletImagePath,fireRate,bulletRelGrav,damage,maxAmmo,isfullauto)
weapons = [
["pistol","Graphics/pistol.png",300,"Graphics/pistolBullet.png",300,10,10,12,False,
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
0,1,"Sounds/9mm.wav"
],
["Assault Rifle","Graphics/ar.png",150,"Graphics/arBullet.png", 600,1,7,30,True,
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
0,1,"Sounds/9mm.wav"
],
["Sniper","Graphics/Sniper.png",400,"Graphics/sniperBullet.png",30,1,30,5,False,
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
0,1,"Sounds/sniperShot.wav"
],
["Shotgun","Graphics/shotgun.png",400,"Graphics/slug.png",200,1,10,6,False,
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
10,6,"Sounds/explosion.wav"
],
["Rpg-7","Graphics/rpg7.png",150,"Graphics/rpg7rocket.png",12,1,50,3,False,
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
0,1,"Sounds/explosion.wav"
],
["MCX","Graphics/MCX.png",300,"Graphics/arBullet.png",600,1,6,30,True,
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
0,1,"Sounds/explosion.wav"
],
["desert Eagle","Graphics/deagle.png",250,"Graphics/pistolBullet.png",120,4,20,7,False,
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
0,1,"Sounds/deagle.wav"
],
["MX250","Graphics/mx250.png",500,"Graphics/arBullet.png",900,1,4,50,True,
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
0,1,"Sounds/machinegun.wav"
]
]

powerUps = [
    {
    "name" : "Double Jump",
    "imagePath" : "Graphics/doubeJump.png",
    "isTimed" : False,
    "time" : 0,
    "modifications" :
    {"maxJumps" : 1,
    "jumpSpeedMod" : 0,
    "speedMod" : 0,
    "maxHealthMod" : 0,
    "healthMod" : 0,
    "damageMultiplierMod" : 0,
    "isInvincible" : False
    }
    },
    {
    "name" : "Big Jump",
    "imagePath" : "Graphics/bigJumpPowerup.png",
    "isTimed" : True,
    "time" : 5,
    "modifications" :
    {"maxJumps" : 0,
    "jumpSpeedMod" : 2,
    "speedMod" : 0,
    "maxHealthMod" : 0,
    "healthMod" : 0,
    "damageMultiplierMod" : 0,
    "isInvincible" : False
    }
    },
    {
    "name" : "Speed",
    "imagePath" : "Graphics/speedPowerUp.png",
    "isTimed" : True,
    "time" : 5,
    "modifications" :
    {"maxJumps" : 0,
    "jumpSpeedMod" : 0,
    "speedMod" : 100,
    "maxHealthMod" : 0,
    "healthMod" : 0,
    "damageMultiplierMod" : 0,
    "isInvincible" : False
    }
    },
    {
    "name" : "heal",
    "imagePath" : "Graphics/heal.png",
    "isTimed" : False,
    "time" : 0,
    "modifications" :
    {"maxJumps" : 0,
    "jumpSpeedMod" : 0,
    "speedMod" : 0,
    "maxHealthMod" : 0,
    "healthMod" : 30,
    "damageMultiplierMod" : 0,
    "isInvincible" : False
    }
    },
    {
    "name" : "Max Health",
    "imagePath" : "Graphics/maxHealthModifier.png",
    "isTimed" : False,
    "time" : 0,
    "modifications" :
    {"maxJumps" : 0,
    "jumpSpeedMod" : 0,
    "speedMod" : 0,
    "maxHealthMod" : 30,
    "healthMod" : 0,
    "damageMultiplierMod" : 0,
    "isInvincible" : False
    }
    },
    {
    "name" : "Damage",
    "imagePath" : "Graphics/DamagePowerup.png",
    "isTimed" : True,
    "time" : 10,
    "modifications" :
    {"maxJumps" : 0,
    "jumpSpeedMod" : 0,
    "speedMod" : 0,
    "maxHealthMod" : 0,
    "healthMod" : 0,
    "damageMultiplierMod" : 0.5,
    "isInvincible" : False
    }
    },
    {
    "name" : "Shield",
    "imagePath" : "Graphics/ShieldPoweup.png",
    "isTimed" : True,
    "time" : 5,
    "modifications" :
    {"maxJumps" : 0,
    "jumpSpeedMod" : 0,
    "speedMod" : 0,
    "maxHealthMod" : 0,
    "healthMod" : 0,
    "damageMultiplierMod" : 0,
    "isInvincible" : True
    }
    }
]

def scaleRect(height : int,rect : tuple):
    scaler = height / 720
    return (rect[0] * scaler, rect[1] * scaler)

def scaleValue(height : int,value : int):
    scaler = height / 720
    return int(value * scaler)

def incDecInt(value : int,change : int,max : int,min : int = 0):
    if(value + change > max):
        return min
    elif(value + change < min):
        return max
    else:
        return value + change

def clip(surface : pygame.Surface, x, y, x_size, y_size): #Get a part of the image
    clipRect = pygame.Rect(x,y,x_size,y_size) #Part of the image
    surface.set_clip(clipRect) #Clip or you can call cropped
    return surface.subsurface(surface.get_clip()) #Get subsurface