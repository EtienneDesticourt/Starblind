import numpy as np
import time, threading
from Game.Entity import Entity
from Game.Player import Player
from Game.Projectile import Projectile
from Game.Impact import Impact
from Resources.Resources import Resources
from Engine.SoundEvent import SoundEvent #TODO: Should it be in game?
from math import hypot

class World(object):
    def __init__(self, delay = 0.005):
        self.delay = delay
        self.entities    = []
        self.projectiles = []
        self.floor = []
        self.impacts = []

    def loadMap(self, mapId):
        mapInfo = Resources._instance.assets[mapId]
        for entityInfo in mapInfo['entities']:
            self.spawnEntity(*entityInfo)
        for tileInfo in mapInfo['floor']:
            self.spawnFloor(*tileInfo)


    #TODO: Clean up all these shitty functions
    def spawnImpact(self, position, impactType, lifespan):
        new = Impact()

    def spawnEntity(self, position, entityType):
        #TODO: Save entity config in resources and query, pass only pos and not rect
        new = Entity(position, entityType)
        self.entities.append(new)
        return new

    def spawnFloor(self, position, entityType):
        new = Entity(position, entityType)
        self.floor.append(new)
        return new

    def spawnPlayer(self, position):
        new = Player(position)
        self.entities.append(new)
        return new

    def spawnProjectile(self, entity):
        #TODO: Implement specific behaviour for projectile.
        #TODO: Don't actually need to check intersection with each other also only contain, not collide
        dx, dy = entity.calcWeaponOffset()
        distance = hypot(dx,dy)
        position = [entity.rect.centerx+dx, entity.rect.centery+dy]
        facing = entity.facingVect
        event = SoundEvent(position, "shot", distance)
        new = Projectile(position, facing)
        self.entities.append(new)
        return new

    def shoot(self):
        for entity in self.entities:
            if entity.shooting:
                currentTime = time.time()
                timeSinceLast = currentTime - entity.lastShot
                if timeSinceLast  > entity.shootingPeriod:
                    self.spawnProjectile(entity)
                    entity.lastShot = time.time()

    def move(self):
        movedRects = [entity.rect.move(*entity.speed) for entity in self.entities]
        copiedRects = movedRects.copy()
        for index in range(len(movedRects)):
            entity = self.entities[index]
            rect   = movedRects[index]

            copiedRects.remove(rect)
            collisions = rect.collidelist(copiedRects)
            if collisions == -1:
                #TODO: Handle floats
                entity.rect.move_ip(*entity.speed)
            else:
                for i in collisions:
                    blockingEntity = self.entities[i]
                    blockingEntity.hit()
                    impactType = blockingEntity.impact()
                    if impactType != None:
                        self.spawnImpact(rect, impactType)

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


