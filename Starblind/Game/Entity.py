from math import hypot, cos, sin, acos, pi, asin, atan2
from Engine.Visual import Visual
from Resources.Resources import Resources

class Entity(object):
    def __init__(self, Rect, entityType):
        self.Rect  = Rect
        self.speed = [0,0]
        self.facing = [0,0]
        self.angle = 90
        self.facingVect = [0, 0]
        self.weaponOffset = [0,-41] #TODO: Put in weapon class
        self.shootingPeriod = 0.07 #TODO: Put in weapon class
        self.accuracyOffset = 0.01 #TODO: Put in weapon class
        self.entityType = entityType
        self.isShooting = False
        self.lastShotTime = 0
        self.canMove = True
        self.canShoot = True
        self.canCollide = True
        self.isVisible = True
        self.isDeadOnImpact = False
        self.removeOnDeath = True
        self.impactType = "blood_impact"
        self.life = 1
        self.damageOnImpact = 0
        self.Visual = Resources._instance.getVisual(entityType)

    def die(self):
        self.life = 0
        self.canMove = False
        self.canCollide = False
        self.canShoot = False

    def isAlive(self):
        return self.life > 0

    def isDead(self):
        return not self.isAlive()

    def impact(self):
        "Returns the type of impact made when it's hit"
        return None

    def hitBy(self, Entity):
        if self.isDead(): return
        self.life -= Entity.damageOnImpact
        if self.isDead():
            self.die()

    def calcWeaponOffset(self): #TODO: Move to shooting entity
        x,y = self.facingVect
        angle = asin( (0*x+1*y)/( hypot(x,y)*hypot(0,1)))
        angle = atan2(-y, x) - 90/180*pi
        x, y = self.weaponOffset
        nx =   x * cos(angle) + y * sin(angle)
        ny = - x * sin(angle) + y * cos(angle)
        return [nx, ny]

