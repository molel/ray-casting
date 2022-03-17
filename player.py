from math import cos, sin

import pygame as pg

from drawing import mapping
from settings import *
from world import walls


class Player:
    def __init__(self):
        self.x, self.y = POS
        self.pov = POV

    def mouse_control(self):
        if pg.mouse.get_focused():

            difference = pg.mouse.get_pos()[0] - HALF_OF_WIDTH
            pg.mouse.set_pos((HALF_OF_WIDTH, HALF_OF_HEIGHT))
            self.pov += difference * 0.004

    def move(self):
        keys = pg.key.get_pressed()
        sin_pov = sin(self.pov)
        cos_pov = cos(self.pov)
        self.pov %= DOUBLE_PI
        self.mouse_control()
        if keys[pg.K_LEFT]:
            self.pov -= 0.035
        if keys[pg.K_RIGHT]:
            self.pov += 0.035
        if keys[pg.K_w]:
            dx = STEP * cos_pov
            dy = STEP * sin_pov
            if mapping(self.x + dx + 30 * cos_pov, self.y + dy + 30 * sin_pov) not in walls:
                self.x += STEP * cos_pov
                self.y += STEP * sin_pov
        if keys[pg.K_s]:
            dx = STEP * cos_pov
            dy = STEP * sin_pov
            if mapping(self.x - dx - 30 * cos_pov, self.y - dy - 30 * sin_pov) not in walls:
                self.x -= STEP * cos_pov
                self.y -= STEP * sin_pov
        if keys[pg.K_a]:
            dx = STEP * sin_pov
            dy = STEP * cos_pov
            if mapping(self.x + dx + 30 * sin_pov, self.y - dy - 30 * cos_pov) not in walls:
                self.x += STEP * sin_pov
                self.y -= STEP * cos_pov
        if keys[pg.K_d]:
            dx = STEP * sin_pov
            dy = STEP * cos_pov
            if mapping(self.x - dx - 30 * sin_pov, self.y + dy + 30 * cos_pov) not in walls:
                self.x -= STEP * sin_pov
                self.y += STEP * cos_pov
