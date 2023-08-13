import pygame as pyg
import numpy as np


class TextureLoader:
    '''
    Texture Loader
    '''
    def __init__(self) -> None:
        self.texture = pyg.image.load(
            "asserts/NES - Battle City JPN - General Sprites.png")

    def get_texture(self) -> pyg.Surface:
        return self.texture

    def get_tank(self,
                 tank_player: int = 0,
                 tank_type: int = 0,
                 dir: int = 0,) -> pyg.Rect:
        # player = 0: user 0
        # player = 1: user 1
        # player = 2: strong ai
        # player = 3: weak ai
        player_offset = np.array([tank_player // 2, tank_player % 2], dtype=np.int32)
        player_offset *= 128
        type_offset = np.array([tank_player // 2, tank_player % 2], dtype=np.int32)
        

        return pyg.Rect(player_offset[0], player_offset[1], 15, 15)

    def get_block(self,
                  block_type: int = 0,
                  damage_type: int = 0):
        pass
