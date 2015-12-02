from Engine.Renderer        import Renderer
from Engine.EventHandler    import EventHandler
from Engine.SoundSystem     import SoundSystem
from Game.World             import World
from Game.Workers.Shooter   import Shooter
from Game.Workers.Mover     import Mover
from Resources.Resources    import Resources
from pygame import Rect
import pygame

#Init engine.
pygame.mixer.pre_init(22050, -16, 2, 512) #TODO: Move this to sound system
pygame.init()
pygame.mixer.set_num_channels(25) #shot lasts 1.5 secs and is used every 0.07 sec -> 21.- channels
SoundSystem  = SoundSystem()
Renderer     = Renderer()
EventHandler = EventHandler()

#Load resources.
Res = Resources()
Res.load()

#Init world and start workers.
World   = World()
Shooter = Shooter(0.01, World)
Mover   = Mover(0.01, World)
Shooter.start()
Mover.start()

#Add player and enemy.
Player = World.spawnPlayer(Rect(380,280,30,30))
Enemy  = World.spawnEntity(Rect(100, 130, 30, 30), "enemy")

#Start engine.
SoundSystem.start()
Renderer.start(World.Entities)
EventHandler.start(Player) #We start the event handler last because it needs to run on the main thread

#Shut down all running threads
print("Quitting.")
EventHandler.quit()
Renderer.quit()
SoundSystem.quit()
Shooter.quit()
Mover.quit()

