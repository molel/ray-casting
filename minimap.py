from math import cos, sin

import pygame as pg

from settings import *


class Minimap:
    def __init__(self, screen, walls, width, height):
        self.sc = screen
        self.walls = {(j // TILE_SIZE, i // TILE_SIZE) for j, i in walls}
        self.width = width * MINIMAP_TILE_SIZE
        self.height = height * MINIMAP_TILE_SIZE

    def draw(self, px, py, ppov):
        pg.draw.rect(self.sc, WHITE, (0, 0, self.width, self.height))
        for j, i in self.walls:
            pg.draw.rect(self.sc, BLACK, (j * MINIMAP_TILE_SIZE, i * MINIMAP_TILE_SIZE,
                                          MINIMAP_TILE_SIZE, MINIMAP_TILE_SIZE))
        pg.draw.circle(self.sc, GREEN, (px * SCALE_MINIMAP, py * SCALE_MINIMAP), 2)
        pg.draw.line(self.sc, GREEN, (px * SCALE_MINIMAP, py * SCALE_MINIMAP), ((px + 50 * cos(ppov)) * SCALE_MINIMAP,
                                      (py + 50 * sin(ppov)) * SCALE_MINIMAP))
