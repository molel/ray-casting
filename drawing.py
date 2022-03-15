from math import sin, cos

import pygame as pg

from settings import *


class Drawing:
    def __init__(self, screen, walls):
        self.screen = screen
        self.walls = walls
        self.img = pg.image.load("img/wall.png").convert()
        self.textures = {0: pg.image.load("img/wall.png").convert()}

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
            xv, dx = (mx + TILE_SIZE, 1) if cos_p >= 0 else (mx, -1)
            for i in range(0, WIDTH, TILE_SIZE):
                dv = (xv - ox) / cos_p
                y = oy + dv * sin_p
                if self.mapping(xv + dx, y) in self.walls:
                    break
                xv += dx * TILE_SIZE

            # Horizontal intersections
            yh, dy = (my + TILE_SIZE, 1) if sin_p >= 0 else (my, -1)
            for i in range(0, WIDTH, TILE_SIZE):
                dh = (yh - oy) / sin_p
                x = ox + dh * cos_p
                if self.mapping(x, yh + dy) in self.walls:
                    break
                yh += dy * TILE_SIZE

            depth, index = (dv, y % TILE_SIZE) if dv <= dh else (dh, x % TILE_SIZE)
            depth *= cos(opov - pov)
            depth = max(depth, 0.00001)
            proj_height = min(PROJ_COEFF / depth, 2 * HEIGHT)
            c = 255 / (1 + depth * depth * 0.00002)
            color = (c, c, c)
            tempSurf = pg.Surface((SCALE_X, HEIGHT))
            tempSurf.blit(self.img, (0, 0), (index * SCALE_TEXTURE, 0, SCALE_TEXTURE, 800))
            tempSurf = pg.transform.scale(tempSurf, (SCALE_X, proj_height))
            self.screen.blit(tempSurf, (ray * SCALE_X, CENTER_HEIGHT - proj_height // 2))
            pov += RAY_STEP
