from math import cos, sin

import pygame as pg

from settings import *


class Player:
    def __init__(self):
        self.x, self.y = POS
        self.pov = POV


    def move(self):
        keys = pg.key.get_pressed()
        sin_pov = sin(self.pov)
        cos_pov = cos(self.pov)
        if keys[pg.K_LEFT]:
            self.pov -= 0.035
        if keys[pg.K_RIGHT]:
            self.pov += 0.035
        if keys[pg.K_w]:
            self.x += STEP * cos_pov
            self.y += STEP * sin_pov
        if keys[pg.K_s]:
            self.x -= STEP * cos_pov
            self.y -= STEP * sin_pov
        if keys[pg.K_a]:
            self.x += STEP * sin_pov
            self.y -= STEP * cos_pov
        if keys[pg.K_d]:
            self.x -= STEP * sin_pov
            self.y += STEP * cos_pov
