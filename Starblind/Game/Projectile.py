from pygame import Rect
from Game.Entity import Entity


class Projectile(Entity):
    """Punctual entity"""
    def __init__(self, position, orientation):
        R = Rect(position[0], position[1], 1, 1)
        super(Projectile, self).__init__(R, "bullet")
        self.speed = [orientation[0]*20, orientation[1]*20]
        self.damageOnImpact = 1 #TODO: make parameter
        self.canShoot = False
        self.removeOnDeath = True
        self.isDeadOnImpact = True


