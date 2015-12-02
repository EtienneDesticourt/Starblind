import time
from Game.Entity import Entity


class Impact(Entity):
    """docstring for Impact"""
    def __init__(self, Rect, impactType, lifespan=0):
        super(Impact, self).__init__(Rect, impactType)
        self.lifespan = lifespan
        self.birth = time.time()
        self.canCollide = False
        self.canMove = False
        self.canShoot = False

    def isAlive(self):
        if not self.lifespan: return True
        else: return time.time() - self.birth < self.lifespan

