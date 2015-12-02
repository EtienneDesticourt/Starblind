import pygame, threading, time
from Resources.Resources import Resources

class Renderer(object):
    def __init__(self, displaySize=(800,600), renderDelay=0.01):
        self.display = self.createDisplay(displaySize)
        self.renderDelay = renderDelay

    def createDisplay(self, displaySize):
        display = pygame.display.set_mode(displaySize)
        return display

    def render(self, Entities):
        for Entity in Entities:
            self.display.blit(Resources._instance.assets[Entity.entityType], Entity.Rect)

    def run(self, Entities):
        while not self.endRun:
            self.display.blit(Resources._instance.assets["background"], (0,0))
            self.render(Entities)
            pygame.display.flip()
            time.sleep(self.renderDelay)

    def start(self, Entities):
        self.endRun = False
        t = threading.Thread(target=self.run, args=[Entities])
        t.start()

    def quit(self):
        self.endRun = True
