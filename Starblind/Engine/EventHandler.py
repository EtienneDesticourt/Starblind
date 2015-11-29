import pygame, threading, time
from pygame.locals import * #Event types

class EventHandler(object):
    """Handles all pygame events"""
    def __init__(self, delay=0.1):
        self.delay = delay

    def handleEvents(self, player):
        for event in pygame.event.get():
            print(event)
            if event.type == KEYDOWN:
                if   event.key == 273:
                    player.goingUp = True
                elif event.key == 274:
                    player.goingDown = True
                elif event.key == 275:
                    player.goingRight = True
                elif event.key == 276:
                    player.goingLeft = True
                elif event.key == 306:
                    player.shooting = True
                player.updateSpeed()
            elif event.type == KEYUP:
                if   event.key == 273:
                    player.goingUp = False
                elif event.key == 274:
                    player.goingDown = False
                elif event.key == 275:
                    player.goingRight = False
                elif event.key == 276:
                    player.goingLeft = False
                elif event.key == 306:
                    player.shooting = False
                player.updateSpeed()
            if event.type == QUIT:
                self.endRun = True

    def run(self, player):
        while not self.endRun:
            self.handleEvents(player)
            time.sleep(self.delay)

    def start(self, player):
        self.endRun = False
        self.run(player)

    def quit(self):
        self.endRun = True



