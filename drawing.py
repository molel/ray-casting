from math import sin, cos

import pygame as pg

from settings import *


class Drawing:
    def __init__(self, screen, walls):
        self.screen = screen
        self.walls = walls
        self.img = pg.image.load("img/wall.png").convert()
        self.textures = {0: pg.image.load("img/wall.png").convert(),
                         "sky": pg.transform.scale(pg.image.load("img/sky.png").convert(), (WIDTH * 2, HALF_OF_HEIGHT))}

    @staticmethod
    def mapping(x, y):
        return (x // TILE_SIZE) * TILE_SIZE, (y // TILE_SIZE) * TILE_SIZE

    def background(self, ppov):
        offset = -2*ppov / DOUBLE_PI * WIDTH
        self.screen.blit(self.textures["sky"], (-WIDTH*2 + offset, 0))
        self.screen.blit(self.textures["sky"], (offset, 0))
        self.screen.blit(self.textures["sky"], (WIDTH*2 + offset, 0))
        pg.draw.rect(self.screen, GRAY, (0, HALF_OF_HEIGHT, WIDTH, HALF_OF_HEIGHT))

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
            proj_height = min(SCALE_PROJECTION / depth, 4 * HEIGHT)
            c = 255 / (1 + depth * depth * 0.00002)
            color = (c, c, c)
            tempSurf = pg.Surface((SCALE_RAY, TEXTURE_HEIGHT))
            tempSurf.blit(self.img, (0, 0), (index * SCALE_TEXTURE, 0, SCALE_TEXTURE, TEXTURE_HEIGHT))
            tempSurf = pg.transform.scale(tempSurf, (SCALE_RAY + 1, proj_height))
            self.screen.blit(tempSurf, (ray * SCALE_RAY, HALF_OF_HEIGHT - proj_height // 2))
            pov += RAY_STEP
