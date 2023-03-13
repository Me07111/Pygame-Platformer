import pygame
from config import clip
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
            animLength = self.animLengths[animIndex]
        else:
            animLength = self.animLengths[self.animIndexOverride]

        if(animIndex != self.previousAnim):
            self.frameIndex = 0
            self.TimeSinceLastFrame = 0
        else:
            self.TimeSinceLastFrame += delta
        
        self.previousAnim = animIndex

        if(self.TimeSinceLastFrame >= self.animSpeeds[animIndex]):
            self.TimeSinceLastFrame = 0
            if(self.frameIndex < animLength - 1):
                self.frameIndex += 1
                if(self.animIndexOverride != -1 and self.frameIndex == animLength - 1):
                    self.animIndexOverride = -1
                    self.frameIndex = 0
            else:
                self.frameIndex = 0
        return clip(self.animations[animIndex],self.frameIndex*self.frameSize[0],0,self.frameSize[0],self.frameSize[1])
        

    
    def playAnim(self,animIndex):
        self.animIndexOverride = animIndex
