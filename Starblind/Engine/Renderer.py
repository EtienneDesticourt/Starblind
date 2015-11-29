import pygame, Resources, threading, time

class Renderer(object):
    def __init__(self, Resources, displaySize=(800,600), renderDelay=0.01):
        self.display = self.createDisplay(displaySize)
        self.renderDelay = renderDelay
        self.Resources = Resources

    def createDisplay(self, displaySize):
        display = pygame.display.set_mode(displaySize)
        return display

    def render(self, entities):
        self.display.blit(self.Resources.assets["background"], (0,0))
        for entity in entities:
            self.display.blit(self.Resources.assets[entity.entityType], entity.rect)

    def run(self, entities):
        while not self.endRun:
            self.render(entities)
            pygame.display.flip()
            time.sleep(self.renderDelay)

    def start(self, entities):
        self.endRun = False
        t = threading.Thread(target=self.run, args=[entities])
        t.start()

    def quit(self):
        self.endRun = True
