from Game.Impact import Impact
from Game.Workers.Worker import Worker

class Mover(Worker):
    """Handles moving the entities"""
    def __init__(self, *args):
        super(Mover, self).__init__(*args)

    def act(self):
        #Go through all the entities that can move
        for MovingEntity in self.World.Entities:
            if not MovingEntity.canMove: continue
            NextRect = MovingEntity.Rect.move(*MovingEntity.speed)
            hasMetObstacle = False
            #Go through all the entities that can be collided with
            for ObstacleEntity in self.World.Entities:
                if not ObstacleEntity.canCollide: continue
                if MovingEntity == ObstacleEntity: continue
                #If they collide, hit the obstacle
                if NextRect.colliderect(ObstacleEntity.Rect):
                    ObstacleEntity.hitBy(MovingEntity)
                    self.World.spawnImpact(ObstacleEntity.Rect, ObstacleEntity.impactType, 0) #TODO: More precise pos
                    hasMetObstacle = True

                    if MovingEntity.isDeadOnImpact:
                        self.World.RemovalQueue.append(MovingEntity)

            #If it didn't collide with anyone move it
            if not hasMetObstacle:
                MovingEntity.Rect = NextRect
