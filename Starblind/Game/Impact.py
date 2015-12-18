import time
from Game.Entity import Entity
from Resources.Resources import Resources

class Impact(Entity):
    """docstring for Impact"""
    def __init__(self, Rect, impactType, lifespan=0):
        super(Impact, self).__init__(Rect, impactType)
        self.lifespan       = lifespan
        self.birth          = time.time()
        self.canCollide     = False
        self.canMove        = False
        self.canShoot       = False
        self.removeOnDeath  = True
        Anim                = Resources._instance.assets[impactType]
        self.lifespan       = Anim.frameDelay * len(Anim.frames)

    def isAlive(self):
        if not self.lifespan: return True
        else: return time.time() - self.birth < self.lifespan

