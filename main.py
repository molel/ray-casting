import pygame as pg

from settings import *
from world import walls

pg.init()
screen = pg.display.set_mode(RES)
clock = pg.time.Clock()
while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            exit()
    screen.fill(BLACK)
    for i, j in walls:
        pg.draw.rect(screen, WHITE, (i * TILE_SIZE, j * TILE_SIZE, TILE_SIZE, TILE_SIZE), 1)

    pg.display.flip()
    clock.tick(FPS)
