from math import cos, sin

import pygame as pg

from player import Player
from settings import *

pg.init()
screen = pg.display.set_mode(RES)
clock = pg.time.Clock()

player = Player()


def mapping(x, y):
    return x // TILE_SIZE * TILE_SIZE, y // TILE_SIZE * TILE_SIZE


while True:

    for event in pg.event.get():
        if event.type == pg.QUIT:
            exit()

    screen.fill(BLACK)

    player.draw(screen)

    for i in range(9):
        pg.draw.line(screen, WHITE, (i * TILE_SIZE, 0), (i * TILE_SIZE, HEIGHT))
        pg.draw.line(screen, WHITE, (0, i * TILE_SIZE), (WIDTH, i * TILE_SIZE))

    ox, oy = player.x, player.y
    mx, my = mapping(player.x, player.y)
    pov = player.pov

    sin_p = sin(pov)
    cos_p = cos(pov)

    sin_p = sin_p if sin_p else 0.00001
    cos_p = cos_p if cos_p else 0.00001
    # Vertical intersections
    x, dx = (mx + TILE_SIZE, TILE_SIZE) if cos_p >= 0 else (mx, -TILE_SIZE)
    for i in range(0, WIDTH, TILE_SIZE):
        dv = (x - ox) / cos_p
        y = oy + dv * sin_p
        pg.draw.circle(screen, (255, 0, 0), (x, y), 3)
        x += dx

    # Horizontal intersections
    y, dy = (my + TILE_SIZE, TILE_SIZE) if sin_p >= 0 else (my, -TILE_SIZE)
    for i in range(0, WIDTH, TILE_SIZE):
        dv = (y - oy) / sin_p
        x = ox + dv * cos_p
        pg.draw.circle(screen, (255, 0, 0), (x, y), 3)
        y += dy

    # ray = player.pov - FOV / 2
    # for _ in range(NUM_OF_RAYS):
    #     pg.draw.line(screen, GREEN, (player.x, player.y),
    #                  (player.x + cos(ray) * DOV, player.y + sin(ray) * DOV))
    #     ray += RAY_STEP

    pg.display.flip()
    clock.tick(FPS)
