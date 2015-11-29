import pygame


class Resources(object):
    """Handles loading/unloading and managin the assets"""
    def __init__(self):
        #TODO: replace assetsToLoad by file
        self.assetsToLoad = [("player",     "Resources/player.png"    ),
                             ("enemy",      "Resources/enemy.png"     ),
                             ("bullet",     "Resources/bullet.png"    ),
                             ("background", "Resources/background.png")]
        self.assets = {}

    def load(self):
        for key, fileName in self.assetsToLoad:
            image = pygame.image.load(fileName)
            self.assets[key] = image
