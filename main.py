import pygame as pg

from drawing import Drawing
from minimap import Minimap
from player import Player
from settings import *
from world import walls, world_map

pg.init()
screen = pg.display.set_mode(RES)
clock = pg.time.Clock()
font = pg.font.SysFont("Arial", 20)

player = Player()
drawing = Drawing(screen, walls)
minimap = Minimap(screen, walls, len(world_map[0]), len(world_map))


def get_fps():
    text = str(int(clock.get_fps()))
    return font.render(text, True, "red")


while True:

    for event in pg.event.get():
        if event.type == pg.QUIT:
            exit()

    drawing.background(player.pov)
    drawing.raycast(player.x, player.y, player.pov)
    player.move()
    minimap.draw(player.x, player.y, player.pov)
    screen.blit(get_fps(), (0, 0))

    pg.display.update()
    clock.tick(FPS)
