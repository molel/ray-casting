from math import sin, cos

import pygame as pg

from settings import *


class Drawing:
    def __init__(self, screen, walls):
        self.screen = screen
        self.walls = walls

    @staticmethod
    def mapping(x, y):
        return (x // TILE_SIZE) * TILE_SIZE, (y // TILE_SIZE) * TILE_SIZE

    def background(self):
        pg.draw.rect(self.screen, LIGHT_BLUE, (0, 0, WIDTH, CENTER_HEIGHT))
        pg.draw.rect(self.screen, GRAY, (0, CENTER_HEIGHT, WIDTH, CENTER_HEIGHT))

    def raycast(self, ox, oy, opov):
        pov = opov - FOV / 2
        mx, my = self.mapping(ox, oy)
        for ray in range(NUM_OF_RAYS):

            sin_p = sin(pov)
            cos_p = cos(pov)

            sin_p = sin_p if sin_p else 0.00001
            cos_p = cos_p if cos_p else 0.00001
            # Vertical intersections
            x, dx = (mx + TILE_SIZE, 1) if cos_p >= 0 else (mx, -1)
            for i in range(0, WIDTH, TILE_SIZE):
                dv = (x - ox) / cos_p
                y = oy + dv * sin_p
                if self.mapping(x + dx, y) in self.walls:
                    break
                x += dx * TILE_SIZE

            # Horizontal intersections
            y, dy = (my + TILE_SIZE, 1) if sin_p >= 0 else (my, -1)
            for i in range(0, WIDTH, TILE_SIZE):
                dh = (y - oy) / sin_p
                x = ox + dh * cos_p
                if self.mapping(x, y + dy) in self.walls:
                    break
                y += dy * TILE_SIZE

            depth = min(dv, dh)
            depth *= cos(opov - pov)
            depth = max(depth, 0.00001)
            proj_height = min(PROJ_COEFF / depth, 2 * HEIGHT)
            c = 255 / (1 + depth * depth * 0.00002)
            color = (c, c, c)
            pg.draw.rect(self.screen, color, (ray * SCALE_X, CENTER_HEIGHT - proj_height // 2, SCALE_X, proj_height))
            pov += RAY_STEP
