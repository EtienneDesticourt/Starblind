import numpy as np
import Entity


class World(object):
    def __init__(self):
        self.characters = np.empty((0), dtype=object)
        self.characterPositions = np.empty((0,2))
        self.characterSpeeds = np.empty((0,2))

        self.projectiles = np.empty((0), dtype=object)
        self.projectilePositions = np.empty((0,2))
        self.projectileSpeeds = np.empty((0,2))

        self.obstacles = np.empty((0,4)) #x1, x2, y1, y2

        #Array to be stacked to main arrays in between update ticks
        self.reinitializeBufferArrays()

    def reinitializeBufferArrays(self):
        self.characterPositionsBuffer = np.empty((0,2))
        self.characterSpeedsBuffer = np.empty((0,2))
        self.projectilePositionsBuffer = np.empty((0,2))
        self.projectileSpeedsBuffer = np.empty((0,2))

    def tick(self):
        #Update positions of entities
        self.updateCharacters()
        collisions = self.updateProjectiles()
        #Remove projectiles that collided and save their impact points
        collidingProjectiles = collisions.any(axis=1)
        self.impacts = np.vstack(self.impacts, self.projectilePositions[collidingProjectiles])
        self.removeProjectiles(collidingProjectiles)
        #Act upon hit rectangles
        collidingRectangles = collisions.any(axis=0)
        #TODO: do something when need be

    def removeProjectiles(self, indexes):
        self.projectiles = self.projectiles[not indexes]
        self.projectilePositions = self.projectilePositions[not indexes]
        self.projectileSpeeds = self.projectileSpeeds[not indexes]

    def removeCharacters(self, indexes):
        self.characters = self.characters[not indexes]
        self.characterPositions = self.characterPositions[not indexes]
        self.characterSpeeds = self.characterSpeeds[not indexes]

    def updateCharacters(self):
        newPositions = self.characterPositions + self.characterSpeeds
        collisions = self.getCollisions(newPositions, self.obstacles)
        colliding = collisions.any(axis=1)
        self.characterPositions[not colliding] = newPositions[not colliding]
        return collisions

    def updateProjectiles(self):
        newPositions = self.projectilePositions + self.projectileSpeeds
        collisions = self.getCollisions(newPositions, self.obstacles) #TODO: Figure out how to check for collisions with characters as well
        colliding = collisions.any(axis=1)
        self.projectilePositions[not colliding] = newPositions[not colliding]
        return collisions

    def getCollisions(self, positions, rectangles):
        #Unpack coordinaties from arrays
        px, py = positions.T
        px = px.reshape((px.size, 1)) #reshaping to get matrices instead of vectors for later calculations
        py = py.reshape((py.size, 1))
        rx1, rx2, ry1, ry2 = rectangles.T

        inXRange = np.logical_and(px >= rx1, px < rx2)
        inYRange = np.logical_and(py >= ry1, py < ry2)
        inRectangle = np.logical_and(inXRange, inYRange)

        return inRectangle

    def getAngles(self, vects1, vects2):
        angles = np.arctan2(vects1[:,1], vects1[:,0]) - np.arctan2(vects2[:,1], vects2[:,0])
        return angles

    def inFieldOfView(self, targetPosition, positions, speeds):
        vects = - (positions - targetPosition)
        #TODO: normalize here
        angles = self.getAngles(vects, speeds)
        facingTarget = angles < 160
        rays = vects[facingTarget].dot(np.linspace(0,100)) #TODO: precreate linspace

    def spawnEntity(self):


    def addCharacter(self, position, speed):
        pass #Pass pos and speed by ref i.e: self.pos = array[id]

    def addProjectile(self, position, speed):
        pass
