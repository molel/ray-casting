import pygame as pg

from drawing import Drawing
from player import Player
from settings import *
from world import walls

pg.init()
screen = pg.display.set_mode(RES)
clock = pg.time.Clock()

player = Player()
drawing = Drawing(screen, walls)

while True:

    for event in pg.event.get():
        if event.type == pg.QUIT:
            exit()

    drawing.background()
    drawing.raycast(player.x, player.y, player.pov)
    player.move()

    pg.display.update()
    clock.tick(FPS)
