from Game.Workers.Worker import Worker
from Engine.Animation import Animation

class Animator(Worker):
    """docstring for Animator"""
    def __init__(self, *args):
        super(Animator, self).__init__(*args)

    def act(self):
        for Entity in self.World.Entities:
            if not isinstance(Entity.Visual, Animation): continue
            Anim = Entity.Visual
            if Anim:
                currentTime = self.time.time()
                if currentTime - Anim.lastFrameTime > Anim.frameDelay:
                    Anim.nextFrame() #TODO: Eventually nextFrame(int) with int = floor of time passed by delay or use modulo
                    Anim.lastFrameTime = currentTime
