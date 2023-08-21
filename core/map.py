import numpy as np
import pygame as pyg
import random
from core.game_object import*
from core.constants import *
from core.texture_loader import *


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

    def get_rect(self):
        return pyg.Rect(self.pos[0], self.pos[1], BLOCK_LENGTH, BLOCK_LENGTH)


    # def display_wall(self):
    #     pass
        # if wall_self.die == False:
        #     window.blit(wall_self.image,wall_self.rect)
        

class Map:
    '''
    Game Map
    '''

    def __init__(self,
                 width=MAP_WIDTH,
                 height=MAP_HEIGHT) -> None:
        self.width = width
        self.height = height
        self.wall_list = []
        # store the map in a numpy array with data type
        self.map = np.zeros((height, width), dtype=np.int32)
        self.init_map()

    def get_map_sizes_in_pixel(self) -> tuple[int, int]:
        return (self.width * BLOCK_LENGTH, self.height * BLOCK_LENGTH)

    def get_boundary_rect(self, i):
        map_size = self.get_map_sizes_in_pixel()
        if i == 0:
            return pyg.Rect(map_size[0], 0, BLOCK_LENGTH, map_size[1])
        elif i == 1:
            return pyg.Rect(0, map_size[1], map_size[0], BLOCK_LENGTH)
        elif i == 2:
            return pyg.Rect(-BLOCK_LENGTH, 0, BLOCK_LENGTH, map_size[1])
        elif i == 3:
            return pyg.Rect(0, -BLOCK_LENGTH, map_size[0], BLOCK_LENGTH)

    # todo:
    # 1. map generation
    #   a. connectivity
    # 2. brick damage 怎么判断是哪种墙体嘞
    # 3. map rendering$

    def init_map(self, brick_num: int=BRICK_NUM):
        self.map[PLAYER_BASE[1], PLAYER_BASE[0]] = BASE_BLOCK
        self.wall_list.append(Wall(pos=(PLAYER_BASE[1] * BLOCK_LENGTH, PLAYER_BASE[0] * BLOCK_LENGTH),
                                   lives=BASE_LIVES,
                                   hp=BASE_HP))

        self.map[AI_BASE[1], AI_BASE[0]] = BASE_BLOCK
        self.wall_list.append(Wall(pos=(AI_BASE[1] * BLOCK_LENGTH, AI_BASE[0] * BLOCK_LENGTH),
                                   lives=BASE_LIVES,
                                   hp=BASE_HP))

        for pos in PLAYER_SPAWN_POINTS + AI_SPAWN_POINTS:
            self.map[pos[1], pos[0]] = SPAWN_POINT_BLOCK

        for pos in PLAYER_BASE_BRICKS + AI_BASE_BRICKS:
            self.map[pos[1], pos[0]] = BRICK_BLOCK
            self.wall_list.append(Wall(pos=(pos[0] * BLOCK_LENGTH, pos[1] * BLOCK_LENGTH),
                                        lives=BRICK_LIVES,
                                        hp=BRICK_HP))
        
        for i in range(brick_num):
            pos = [random.randint(0, self.width - 1), random.randint(0, self.height - 1)]
            while (self.map[pos[1], pos[0]] != EMPYT_BLOCK):
                pos = [random.randint(0, self.width - 1), random.randint(0, self.height - 1)]
            self.map[pos[1], pos[0]] = BRICK_BLOCK
            self.wall_list.append(Wall(pos=(pos[0] * BLOCK_LENGTH, pos[1] * BLOCK_LENGTH),
                                        lives=BRICK_LIVES,
                                        hp=BRICK_HP))




# 下划线分割:
# 局部变量
# 成员变量: self.balabala
# 成员函数 (方法)
# visual_studio_live_share
# 驼峰分割
# VisualStudioLiveShare
# 类的名称: TextureLoader, GameObject
# visualStudioLiveShare
# 成员变量: self.visualStudioLiveShare

