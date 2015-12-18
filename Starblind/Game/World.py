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
    """Holds the world's objects."""
    def __init__(self):
        self.Entities = []
        self.RemovalQueue = [] #TODO: implement remover worker
        #TODO: Add non interactive entity/ visual only entity list to speed up rendering, moving, shooting etc

    def spawnEntity(self, Rect, entityType):
        #print(len(self.Entities))
        self.Entities.append(Entity(Rect, entityType))

    def spawnProjectile(self, position, orientation):
        print("Entities:", len(self.Entities))
        print("RemovalQueue:", len(self.RemovalQueue))
        distance = hypot(self.Player.Rect.centerx - position[0], self.Player.Rect.centery - position[1])
        SoundEvent(position, "shot", distance)
        self.Entities.append(Projectile(position, orientation))

    def spawnImpact(self, Rect, impactType, lifeSpan):
        #print(len(self.Entities))
        self.Entities.append(Impact(Rect, impactType, 0))

    def spawnPlayer(self, Rect):
        #print(len(self.Entities))
        P = Player(Rect)
        self.Entities.append(P)
        self.Player = P
        return P


