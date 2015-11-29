from pygame import Rect
from Game.Entity import Entity


class Projectile(Entity):
    """Punctual entity"""
    def __init__(self, position, orientation):
        rect = Rect(position[0], position[1], 1, 1)
        super(Projectile, self).__init__(rect, "bullet")
        self.speed = [orientation[0]*1, orientation[1]*1]

