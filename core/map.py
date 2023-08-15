import numpy as np
import pygame as pyg
from core.game_object import*
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
    # 2. brick damage 怎么判断是哪种墙体嘞
class Wall(GameObject):
    def __init__(self,
                 pos: tuple[float, float],
                 lives:int=16,
                 hp:float = 50) -> None:
        super().__init__(is_dynamic=False,
                         lives=lives,
                         max_hp=hp,
                         pos=pos)
        self.state = (1 << 16) - 1
        self.hps = [hp for i in range(16)]

    def intersect(self, bullet):
        '''
        get hit point of a bullet
        '''
        pass

    def get_hit(self,
                damage:float,
                hit_pos: tuple[float, float] # normalized coordinate
                ):
        if self.hp == 0 or damage <= 0:
            return
        self.hp -= damage
        if self.hp < 0:
            self.hp = 0
            self.lives -= 1
            if self.lives == 0:
                self.die = True

    def displayWall(self):
        pass
        # if wall_self.die == False:
        #     window.blit(wall_self.image,wall_self.rect)
        

    # 3. map rendering$
