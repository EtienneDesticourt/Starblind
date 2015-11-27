import pygame, Resources, World

class Renderer(object):
    def __init__(self):
        self.display = self.createDisplay(dispaySize)
        self.camera = self.createCamera()
        self.renderDelay = renderDelay

    def createCamera(self):
        return World.spawnEntity()


    def createDisplay(self, diplaySize):
        diplay = pygame.display.set_mode(display_size)
        return display

    def render(self, characters):
        for character in characters:
            self.display.blit(character.pos, Resources.Collection[character.resourceId])
        time.sleep(sef.renderDelay)

