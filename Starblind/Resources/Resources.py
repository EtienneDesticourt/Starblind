import pygame, os
from Engine.Visual import Visual
from Engine.Animation import Animation

class Resources(object):
    """Handles loading/unloading and managin the assets"""
    _instance = None
    def __init__(self):
        #TODO: replace assetsToLoad by file
        self.assetsToLoad = [("player",             "Resources/player.png"         ),
                             ("enemy",              "Resources/enemy.png"          ),
                             ("bullet",             "Resources/bullet.png"         ),
                             ("shot",               "Resources/shot.ogg"           ),
                             ("impact",             "Resources/impact.png"         ),
                             ("blood_impact",       ["Resources/blood_impact_0.png",
                                                     "Resources/blood_impact_1.png",
                                                     "Resources/blood_impact_2.png",
                                                     "Resources/blood_impact_3.png",
                                                     "Resources/blood_impact_4.png",
                                                     "Resources/blood_impact_5.png"]),
                             ("background",         "Resources/background.png"     ),
                             ("chapter1_scene1",    "Resources/chapter1_scene1.map"),]
        self.assets = {}
        Resources._instance = self

    def getVisual(self, assetKey):
        return self.assets[assetKey] #Figure out how to give animation copy here

    def loadImage(self, path):
        return Visual(pygame.image.load(path))

    def loadSound(self, path):
        return pygame.mixer.Sound(path)

    def loadAnimation(self, framePaths):
        frames = [pygame.image.load(path) for path in framePaths]#TODO: Add .anim file with timing, paths, etc instead of raw paths
        DELAY = 0.1 #TODO: REMOVE
        LOOP = True #TODO: REMOVE
        return Animation(frames, DELAY, LOOP)


    def load(self): #TODO: addindividual loading functions and asset identification function
        for key, fileName in self.assetsToLoad:
            if isinstance(fileName, list):
                self.assets[key] = self.loadAnimation(fileName)
            else:
                name, ext = os.path.splitext(fileName)
                if ext == ".png":
                    self.assets[key] = self.loadImage(fileName)
                elif ext == ".ogg":
                    self.assets[key] = self.loadSound(fileName)
                elif ext == ".map":
                    pass





