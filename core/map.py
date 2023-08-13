import numpy as np
import pygame as pyg

class Map:
    '''
    Game Map
    '''
    def __init__(self,
                 width=13,
                 height=13,
                 block_length_in_pixel=15) -> None:
        self.width = width
        self.height = height
        self.block_length = block_length_in_pixel
        self.map = np.zeros((height, width), dtype=np.int32)

    def get_surfaces(self):
        pass

    def get_map_sizes_in_pixel(self) -> tuple[int, int]:
        return (self.width*self.block_length, self.height*self.block_length)
    
    def render_solid_layer(self, surface:pyg.Surface):
        for y in range(self.height):
            for x in range(self.width):
                pyg.draw.rect(surface, pyg.Color())
    # todo: 
    # 1. map generation
    #   a. connectivity
    # 2. brick damage
    def get_bricks(self):
        
    # 3. map rendering$