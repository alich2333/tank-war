import numpy as np
import pygame as pyg

from core.constants import *


class Map:
    '''
    Game Map
    '''

    def __init__(self,
                 width=MAP_WIDTH,
                 height=MAP_HEIGHT) -> None:
        self.width = width
        self.height = height
        self.map = np.zeros((height, width), dtype=np.int32)

    def get_surfaces(self):
        pass

    def get_map_sizes_in_pixel(self) -> tuple[int, int]:
        return (self.width * BLOCK_LENGTH, self.height * BLOCK_LENGTH)

    def render_solid_layer(self, surface: pyg.Surface):
        for y in range(self.height):
            for x in range(self.width):
                pyg.draw.rect(surface, pyg.Color())
    # todo:
    # 1. map generation
    #   a. connectivity
    # 2. brick damage

    def get_bricks(self):
        pass
    # 3. map rendering
