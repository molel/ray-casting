from math import cos, sin

import pygame as pg

from player import Player
from settings import *
from world import walls

pg.init()
screen = pg.display.set_mode(RES)
clock = pg.time.Clock()

player = Player()


def mapping(x, y):
    return (x // TILE_SIZE) * TILE_SIZE, (y // TILE_SIZE) * TILE_SIZE


while True:

    for event in pg.event.get():
        if event.type == pg.QUIT:
            exit()

    screen.fill(BLACK)

    player.draw(screen)

    ox, oy = player.x, player.y
    mx, my = mapping(player.x, player.y)
    pov = player.pov - FOV / 2
    for _ in range(NUM_OF_RAYS):

        sin_p = sin(pov)
        cos_p = cos(pov)

        sin_p = sin_p if sin_p else 0.00001
        cos_p = cos_p if cos_p else 0.00001
        # Vertical intersections
        x, dx = (mx + TILE_SIZE, 1) if cos_p >= 0 else (mx, -1)
        for i in range(0, WIDTH, TILE_SIZE):
            dv = (x - ox) / cos_p
            y = oy + dv * sin_p
            if mapping(x + dx, y) in walls:
                break
            x += dx * TILE_SIZE

        # Horizontal intersections
        y, dy = (my + TILE_SIZE, 1) if sin_p >= 0 else (my, -1)
        for i in range(0, WIDTH, TILE_SIZE):
            dh = (y - oy) / sin_p
            x = ox + dh * cos_p
            if mapping(x, y + dy) in walls:
                break
            y += dy * TILE_SIZE

        depth = min(dv, dh)
        pg.draw.line(screen, (255, 0, 0), (ox, oy), (ox + depth * cos_p, oy + depth * sin_p), 3)
        pov += RAY_STEP
    pg.display.flip()
    clock.tick(FPS)
