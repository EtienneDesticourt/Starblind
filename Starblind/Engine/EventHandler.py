import pygame, threading, time
from pygame.locals import * #Event types
from math import atan2, hypot

class EventHandler(object):
    """Handles all pygame events"""
    def __init__(self, delay=0.1):
        self.delay = delay

    def handleEvents(self, player):
        for event in pygame.event.get():
            #print(event)
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
            elif event.type == MOUSEMOTION:
                x, y = player.rect.centerx, player.rect.centery
                x1, y1 = event.pos
                vect = (x1-x, y1-y)
                norm = hypot(*vect)
                player.facingVect = [vect[0]/norm, vect[1]/norm]




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



