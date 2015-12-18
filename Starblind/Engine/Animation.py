from Engine.Visual import Visual
import time

class Animation(Visual):
    """Handles the animation logic for sprites."""
    def __init__(self, frames, delay, loop=False, time=time):
        super(Animation, self).__init__(None)
        self.currentFrame = 0
        self.frames = frames
        self.frameDelay = delay
        self.loop = loop
        self.time = time
        self.lastFrameTime = self.time.time()

    def get(self):
        return self.frames[self.currentFrame]

    def nextFrame(self):
        self.currentFrame += 1
        if self.currentFrame >= len(self.frames):
            if self.loop: self.currentFrame = 0
            else: self.currentFrame -= 1 #Keep at last frame forever if it doesn't loop
        self.lastFrameTime = self.time.time()


