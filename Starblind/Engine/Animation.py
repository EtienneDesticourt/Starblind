from Resources.Resources import Resources
import time

class Animation(object):
    """Handles the animation logic for sprites."""
    def __init__(self, resourceId, delay, time=time):
        self.currentFrame = 0
        self.frames = Resources._instance.assets[resourceId]
        self.frameDelay = delay
        self.time = time
        self.lastFrameTime = self.time.time()

    def nextFrame(self):
        self.currentFrame += 1
        if self.currentFrame >= len(self.frames):
            self.currentFrame = 0
        self.lastFrameTime = self.time.time()


