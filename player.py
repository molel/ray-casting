import pygame as pg

from settings import *


class Player:
    def __init__(self):
        self.x, self.y = POS

    def draw(self, screen):
        pg.draw.circle(screen, WHITE, (self.x, self.y), 4)
