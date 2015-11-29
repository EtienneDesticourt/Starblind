import pygame, threading, time
from Resources.Resources import Resources


class SoundSystem(object):
    """Interface for the pygame mixer"""
    _instance = None
    def __init__(self, delay=0.01):
        super(SoundSystem, self).__init__()
        self.eventQueue = []
        self.delay = delay
        SoundSystem._instance = self

    def calcVolume(self, distance):
        volume = (1000 - distance) / 1000.
        if volume < 0: return 0
        return volume

    def handleEvents(self):
        for event in self.eventQueue:
            #Play
            volume = self.calcVolume(event.distance) - 0.95
            Sound = Resources._instance.assets[event.eventType]
            Sound.set_volume(volume)
            Sound.play()
            #Discard
            self.eventQueue.remove(event)

    def run(self):
        while not self.endRun:
            self.handleEvents()
            time.sleep(self.delay)

    def start(self):
        self.endRun = False
        t = threading.Thread(target=self.run)
        t.start()

    def quit(self):
        self.endRun = True
