

class Entity(object):
    def __init__(self, rect, entityType):
        self.rect  = rect
        self.speed = [0,0]
        self.facing = [0,0]
        self.facingVect = [0,0]
        self.entityType = entityType
        self.shooting = False
        self.shootingPeriod = 1
        self.lastShot = 0

