from Game.Impact import Impact
from Game.Workers.Worker import Worker
import random

class Shooter(Worker):
    """Handles making the entities shoot."""
    def __init__(self, *args):
        super(Shooter, self).__init__(*args)

    def work(self):
        for Entity in self.World.Entities:
            if Entity.canShoot and Entity.isShooting:
                #Check if enough time has passed since last shot
                currentTime  = self.time.time()
                timeSinceLastShot = currentTime - Entity.lastShotTime
                if timeSinceLastShot > Entity.shootingPeriod:
                    #Shoot
                    dx, dy = Entity.calcWeaponOffset()
                    x = Entity.Rect.centerx + dx
                    y = Entity.Rect.centery + dy
                    vx, vy = Entity.facingVect
                    vx += Entity.accuracyOffset * random.randrange(-50, 50) / 100.
                    vy += Entity.accuracyOffset * random.randrange(-50, 50) / 100.
                    self.World.spawnProjectile((x,y), [vx, vy])
                    Entity.lastShotTime = self.time.time()
