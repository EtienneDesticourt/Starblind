from Engine.SoundSystem import SoundSystem

class SoundEvent(object):
    """docstring for SoundEvent"""
    def __init__(self, position, eventType, distance):
        super(SoundEvent, self).__init__()
        self.position = position
        self.eventType = eventType
        self.distance = distance
        SoundSystem._instance.eventQueue.append(self)
