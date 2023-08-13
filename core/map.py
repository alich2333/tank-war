import numpy as np
import pygame as pyg

window = pyg.display.set_mode((500, 200))

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
    # 2. brick damage 怎么判断是哪种墙体嘞
class Wall():
    def __init__(wall_self,
                left,
                top,
                wall_hp:float = 3,
                wall_lives:int = 1) -> None:
        wall_self.image = pyg.image.load('img/steels.gif')
        wall_self.rect = wall_self.image.get_rect()
        wall_self.rect.left = left            
        wall_self.rect.top = top
        wall_self.hp = wall_hp
        wall_self.lives = wall_lives

    def get_hit(wall_self,damage:float):
        if wall_self.hp == 0 or damage <= 0:
            return
        wall_self.hp -= damage
        if wall_self.hp < 0:
            wall_self.hp = 0
            wall_self.lives -= 1
            if wall_self.lives == 0:
                wall_self.die = True

    def displayWall(wall_self):
        if wall_self.die == False:
            window.blit(wall_self.image,wall_self.rect)
        

    # 3. map rendering$