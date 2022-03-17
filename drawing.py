from math import sin, cos

import pygame as pg

from settings import *


def mapping(x, y):
    return (x // TILE_SIZE) * TILE_SIZE, (y // TILE_SIZE) * TILE_SIZE


class Drawing:
    def __init__(self, screen, walls):
        self.screen = screen
        self.walls = walls
        self.img = pg.image.load("img/wall.png").convert()
        self.textures = {0: pg.image.load("img/wall.png").convert(),
                         "sky": pg.transform.scale(pg.image.load("img/sky.png").convert(), (WIDTH * 2, HALF_OF_HEIGHT))}

    def background(self, ppov):
        offset = -2 * ppov / DOUBLE_PI * WIDTH
        self.screen.blit(self.textures["sky"], (-WIDTH * 2 + offset, 0))
        self.screen.blit(self.textures["sky"], (offset, 0))
        self.screen.blit(self.textures["sky"], (WIDTH * 2 + offset, 0))
        pg.draw.rect(self.screen, GRAY, (0, HALF_OF_HEIGHT, WIDTH, HALF_OF_HEIGHT))

    def raycast(self, ox, oy, opov):
        pov = opov - FOV / 2
        mx, my = mapping(ox, oy)
        for ray in range(NUMBER_OF_RAYS):

            psin = sin(pov)
            pcos = cos(pov)

            psin = psin if psin else 0.00001
            pcos = pcos if pcos else 0.00001

            # Vertical intersections
            vx, dx = (mx + TILE_SIZE, 1) if pcos >= 0 else (mx, -1)
            for i in range(0, WIDTH, TILE_SIZE):
                dv = (vx - ox) / pcos
                y = oy + dv * psin
                if mapping(vx + dx, y) in self.walls:
                    break
                vx += dx * TILE_SIZE

            # Horizontal intersections
            hy, dy = (my + TILE_SIZE, 1) if psin >= 0 else (my, -1)
            for i in range(0, WIDTH, TILE_SIZE):
                dh = (hy - oy) / psin
                x = ox + dh * pcos
                if mapping(x, hy + dy) in self.walls:
                    break
                hy += dy * TILE_SIZE

            depth, offset = (dv, y // 1 % TILE_SIZE) if dv <= dh else (dh, x // 1 % TILE_SIZE)
            depth *= cos(opov - pov)
            depth = max(depth, 0.00001)
            projection_height = min(PROJECTION_SCALE / depth, 3 * HEIGHT)

            wall = self.textures[0].subsurface((offset * TEXTURE_SCALE, 0, TEXTURE_SCALE, TEXTURE_HEIGHT))
            wall = pg.transform.scale(wall, (RAY_WIDTH + 1, projection_height))
            self.screen.blit(wall, (ray * RAY_WIDTH, HALF_OF_HEIGHT - projection_height // 2))

            pov += DELTA_RAY
