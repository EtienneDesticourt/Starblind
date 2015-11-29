import Engine.Renderer
import Engine.EventHandler
import Game.World
import Resources.Resources
import pygame

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
Renderer = Engine.Renderer.Renderer(Res)
E = Engine.EventHandler.EventHandler()

W.start()
Renderer.start(W.entities)
E.start(Player)

Renderer.quit()
W.quit()
#E.quit()
