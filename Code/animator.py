import pygame

class Animator:
    def __init__(self,animations : list[pygame.Surface] ,frameSize : tuple, animSpeeds : list[int]):
        self.animations = animations
        self.frameIndex = 0
        self.frameSize = frameSize
        self.animSpeeds = animSpeeds
        self.TimeSinceLastFrame = 0
        self.previousAnim = animations[0]
        self.animLengths = []
        for anim in animations:
            self.animLengths.append(int(anim.get_width() / frameSize[0]))
        self.animIndexOverride = -1 

    def animate(self,animIndex,delta) -> pygame.Surface:
        if(self.animIndexOverride == -1):
            anim = self.animations[animIndex]
            animLength = self.animLengths[animIndex]
        else:
            anim = self.animations[self.animIndexOverride]
            animLength = self.animLengths[self.animIndexOverride]

        if(anim != self.previousAnim):
            self.frameIndex = 0
            self.TimeSinceLastFrame = 0
        else:
            self.TimeSinceLastFrame += delta
        
        self.previousAnim = anim
        if(self.TimeSinceLastFrame >= self.animSpeeds[animIndex]):
            if(self.frameIndex < animLength - 1):
                self.frameIndex += 1
                if(self.animIndexOverride != -1 and self.frameIndex == animLength - 1):
                    self.animIndexOverride = -1
                    self.frameIndex = 0
            else:
                self.frameIndex = 0
        return self.clip(self.animations[animIndex],self.frameIndex*self.frameSize[0],0,self.frameSize[0],self.frameSize[1])
        
    

    def clip(self,surface : pygame.Surface, x, y, x_size, y_size): #Get a part of the image
        clipRect = pygame.Rect(x,y,x_size,y_size) #Part of the image
        surface.set_clip(clipRect) #Clip or you can call cropped
        return surface.subsurface(surface.get_clip()) #Get subsurface
    
    def playAnim(self,animIndex):
        self.animIndexOverride = animIndex
