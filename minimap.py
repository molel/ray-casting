from math import cos, sin

import pygame as pg

from settings import *


class Minimap:
    def __init__(self, screen, walls, width, height):
        self.sc = screen
        self.walls = {(j // TILE_SIZE, i // TILE_SIZE) for j, i in walls}
        self.tile_width = MINIMAP_WIDTH / width
        self.tile_height = MINIMAP_WIDTH / height
        self.width = width * TILE_SIZE
        self.height = height * TILE_SIZE

    def draw(self, px, py, ppov):
        pg.draw.rect(self.sc, WHITE, (0, 0, MINIMAP_WIDTH, MINIMAP_HEIGHT))
        for j, i in self.walls:
            pg.draw.rect(self.sc, BLACK, (j * self.tile_width, i * self.tile_height,
                                          self.tile_width + 1, self.tile_height + 1))
        pg.draw.circle(self.sc, GREEN, (px * MINIMAP_WIDTH / self.width, py * MINIMAP_HEIGHT / self.height), 4)
        pg.draw.line(self.sc, GREEN, (px * MINIMAP_WIDTH / self.width, py * MINIMAP_HEIGHT / self.height),
                     (px * MINIMAP_WIDTH / self.width + 25 * cos(ppov) * MINIMAP_SCALE,
                      py * MINIMAP_HEIGHT / self.height + 25 * sin(ppov) * MINIMAP_SCALE), 2)
