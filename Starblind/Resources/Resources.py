import pygame, os


class Resources(object):
    """Handles loading/unloading and managin the assets"""
    _instance = None
    def __init__(self):
        #TODO: replace assetsToLoad by file
        self.assetsToLoad = [("player",     "Resources/player.png"    ),
                             ("enemy",      "Resources/enemy.png"     ),
                             ("bullet",     "Resources/bullet.png"    ),
                             ("shot",       "Resources/shot.ogg"),
                             ("shotShort",  "Resources/shotShort.ogg"),
                             ("background", "Resources/background.png")]
        self.assets = {}
        Resources._instance = self

    def load(self):
        for key, fileName in self.assetsToLoad:
            name, ext = os.path.splitext(fileName)
            if ext == ".png":
                image = pygame.image.load(fileName)
                self.assets[key] = image
            elif  ext == ".ogg":
                sound = pygame.mixer.Sound(fileName)
                self.assets[key] = sound

