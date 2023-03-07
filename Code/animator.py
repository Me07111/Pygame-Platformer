import pygame

class Animator:
    def __init__(self,animations : list[pygame.Surface] ,frameSize : tuple, animSpeed : int):
        self.animations = animations
        self.frameIndex = 0
        self.frameSize = frameSize
        self.animSpeed = animSpeed
        self.TimeSinceLastFrame = 0
        self.previousAnim = animations[0]
        self.animLengths = []
        for anim in animations:
            self.animLengths.append(anim.get_width() / frameSize[0])

    def animate(self,animIndex,delta):
        anim = self.animations[animIndex]
        animLength = self.animLengths[animIndex]

        if(anim != self.previousAnim):
            self.frameIndex = 0
            self.TimeSinceLastFrame = 0

        self.TimeSinceLastFrame += delta
        if(self.TimeSinceLastFrame >= self.animSpeed):
            if(self.frameIndex <= animLength):
                self.frameIndex += 1
            else:
                self.frameIndex = 0

        return self.clip(self.frameIndex*self.frameSize[0],0,self.frameSize[0],self.frameSize[1])
        
    

    def clip(surface, x, y, x_size, y_size): #Get a part of the image
        handle_surface = surface.copy() #Sprite that will get process later
        clipRect = pygame.Rect(x,y,x_size,y_size) #Part of the image
        handle_surface.set_clip(clipRect) #Clip or you can call cropped
        image = surface.subsurface(handle_surface.get_clip()) #Get subsurface
        return image.copy() #Return