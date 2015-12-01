import time
from Game.Entity import Entity


class Impact(Entity):
    """docstring for Impact"""
    def __init__(self, position, impactType, lifespan=0):
        super(Impact, self).__init__(position, impactType)
        self.lifespan = lifespan
        self.birth = time.time()

    def isAlive(self):
        if not self.lifespan: return True
        else: return time.time() - self.birth < self.lifespan

