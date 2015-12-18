from Game.Impact import Impact
from Game.Workers.Worker import Worker

class Remover(Worker):
    """Handles moving the entities"""
    def __init__(self, *args):
        super(Remover, self).__init__(*args)

    def work(self):
        for Entity in self.World.Entities:
            if Entity.removeOnDeath and Entity.isDead() and not Entity in self.World.RemovalQueue:
                self.World.RemovalQueue.append(Entity)
        for Entity in self.World.RemovalQueue:
            self.World.Entities.remove(Entity) #TODO: figure out how safe this is ( i.e not much)
            self.World.RemovalQueue.remove(Entity)

