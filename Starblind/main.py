import Engine.Renderer
import Engine.EventHandler
import Game.World
import Resources.Resources
import Engine.SoundSystem
import pygame


#TODO: Move this to sound system
pygame.mixer.pre_init(22050, -16, 2, 512)
pygame.init()
pygame.mixer.set_num_channels(25) #shot lasts 1.5 secs and is used every 0.07 sec -> 21.- channels




#pygame.mixer.init(channels=10, buffer=128)
S = Engine.SoundSystem.SoundSystem()
S.start()


W = Game.World.World()

#Spawn player
r = pygame.Rect(380,280,30,30)
Player = W.spawnPlayer(r)
#Spawn enemy
r = pygame.Rect(100,130,30,30)
t = "enemy"
W.spawnEntity(r, t)


Res = Resources.Resources.Resources()
Res.load()
Renderer = Engine.Renderer.Renderer()
E = Engine.EventHandler.EventHandler()

W.start()
Renderer.start(W.entities)
E.start(Player)

Renderer.quit()
W.quit()
E.quit()
S.quit()
