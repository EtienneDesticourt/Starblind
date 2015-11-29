import numpy as np
import time, threading
from Game.Entity import Entity
from Game.Player import Player
from Game.Projectile import Projectile

class World(object):
    def __init__(self, delay = 0.005):
        self.delay = delay
        self.entities    = []
        self.projectiles = []

    def spawnEntity(self, position, entityType):
        #TODO: Save entity config in resources and query, pass only pos and not rect
        new = Entity(position, entityType)
        self.entities.append(new)
        return new

    def spawnPlayer(self, position):
        new = Player(position)
        self.entities.append(new)
        return new

    def spawnProjectile(self, position):
        #TODO: Implement specific behaviour for projectile.
        #TODO: Don't actually need to check intersection with each other also only contain, not collide
        new = Projectile(position,[0.6,0.6])
        self.entities.append(new)
        return new

    def shoot(self):
        currentTime = time.time()
        for entity in self.entities:
            if entity.shooting:
                if currentTime - entity.lastShot > entity.shootingPeriod:
                    self.spawnProjectile((entity.rect.centerx, entity.rect.centery))
                    entity.lastShot = currentTime

    def move(self):
        movedRects = [entity.rect.move(*entity.speed) for entity in self.entities]
        copiedRects = movedRects.copy()
        for index in range(len(movedRects)):
            entity = self.entities[index]
            rect   = movedRects[index]

            copiedRects.remove(rect)
            collisions = rect.collidelist(copiedRects)
            if collisions == -1:
                entity.rect.move_ip(*entity.speed)
            copiedRects.append(rect)

    def run(self): #TODO: Move this to mover?
        while not self.endRun:
            self.move()
            self.shoot() #TODO: put in separate thread
            time.sleep(self.delay)

    def start(self):
        self.endRun = False
        t = threading.Thread(target=self.run)
        t.start()

    def quit(self):
        self.endRun = True


