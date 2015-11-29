from Engine.SoundEvent import SoundEvent
import Resources, pygame


class SoundSystem(object):
    """Interface for the pygame mixer"""
    def __init__(self):
        super(SoundSystem, self).__init__()
        self.eventQueue = []
        pygame.mixer.init()

    def addEvent(self, position, distance, eventType):
        event = SoundEvent(position, eventType, Sound, distance)
        self.eventQueue.append(event)

    def calcVolume(self, distance):
        return (1000 - distance) / 1000.

    def handleEvents(self):
        for event in self.eventQueue:
            #Play
            volume = self.calcVolume(event.distance)
            event.Sound.set_volume(volume)
            event.Sound.play()
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
