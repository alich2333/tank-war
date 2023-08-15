import pygame as pyg
import numpy as np

from core.constants import *


class TextureLoader:
    '''
    Texture Loader
    '''

    def __init__(self) -> None:
        self.main_texture = pyg.image.load(
            "asserts/NES - Battle City JPN - General Sprites.png")
        self.tank_body_textures = [
            pyg.image.load(
                "asserts/Cybertank Artwork/artwork/tank body_red.png"),
            pyg.image.load(
                "asserts/Cybertank Artwork/artwork/tank body_teal.png")]
        self.tank_turret_textures = [
            pyg.image.load(
                "asserts/Cybertank Artwork/artwork/tank turret_red.png"),
            pyg.image.load(
                "asserts/Cybertank Artwork/artwork/tank turret_teal.png")]
        self.tank_body_sizes = [np.zeros(2, dtype=np.float32),
                                np.zeros(2, dtype=np.float32)]
        self.tank_turret_sizes = [np.zeros(2, dtype=np.float32),
                                  np.zeros(2, dtype=np.float32)]
        # load block textures
        # block = 0: brick
        # block = 1: steel brick
        # block = 2: bush
        # block = 3: water
        self.block_textures = []
        for block_type in range(4):
            block_offset = np.zeros(2, dtype = np.int32)
            block_offset[0] = 256
            if block_type == 0:
                pass
            elif block_type == 1:
                block_offset[1] += 16
            elif block_type == 2:
                block_offset[0] += 16
                block_offset[1] += 32
            else:
                block_offset[1] += 48
            tmp = self.main_texture.subsurface((block_offset[0], block_offset[1]), (16, 16))
            self.block_textures.append(pyg.transform.scale(tmp, (BLOCK_LENGTH, BLOCK_LENGTH)))


        # scale player tanks
        for player in range(2):
            body_scale = self.tank_body_textures[player].get_rect()
            turret_scale = self.tank_turret_textures[player].get_rect()
            scale_x = BLOCK_LENGTH / body_scale[3]

            # scale and darken tank body
            self.tank_body_textures[player] = pyg.transform.scale(
                self.tank_body_textures[player],
                (BLOCK_LENGTH, BLOCK_LENGTH))
            tmp = self.tank_body_textures[player].copy()
            tmp.fill(pyg.Color(180, 180, 180, 255))
            self.tank_body_textures[player].blit(
                tmp, (0, 0), None, pyg.BLEND_MULT)

            # scale tank turret
            scale_x *= TURRET_SCALE
            self.tank_turret_textures[player] = pyg.transform.scale(
                self.tank_turret_textures[player],
                (turret_scale[2] * scale_x, turret_scale[3] * scale_x))
            body_rect = self.tank_body_textures[player].get_rect()
            turret_rect = self.tank_turret_textures[player].get_rect()
            self.tank_body_sizes[player][0] = body_rect[2]
            self.tank_body_sizes[player][1] = body_rect[3]
            self.tank_turret_sizes[player][0] = turret_rect[2]
            self.tank_turret_sizes[player][1] = turret_rect[3]

    def get_main_texture(self) -> pyg.Surface:
        return self.main_texture

    def get_player_tank_body_texture(self, player: int, dir: int = 0):
        result = pyg.transform.rotate(
            self.tank_body_textures[player], angle=90 * (dir - 1))
        return result

    def get_player_tank_turret_texture_and_offset(self, player: int, angle: float):
        angle -= 0.5 * np.pi
        angle -= np.floor(angle / (2 * np.pi)) * 2 * np.pi
        c_ = np.cos(angle)
        s_ = np.sin(angle)

        turret_size = self.tank_turret_sizes[player]
        center_offset = turret_size / 2
        center_offset[0] -= 0.25  # offset of the texture
        center_offset[1] += 2  # offset of the texture
        origin_offset = np.zeros_like(center_offset)
        body_offset = self.tank_body_sizes[player] / 2

        if angle <= 0.5 * np.pi:
            origin_offset[1] = s_ * turret_size[0]
        elif angle <= np.pi:
            origin_offset[0] = -c_ * turret_size[0]
            origin_offset[1] = s_ * turret_size[0] - c_ * turret_size[1]
        elif angle < 1.5 * np.pi:
            origin_offset[0] = -c_ * turret_size[0] - s_ * turret_size[1]
            origin_offset[1] = -c_ * turret_size[1]
        else:
            origin_offset[0] = -s_ * turret_size[1]
        rotation = np.array(
            [[c_, s_],
             [-s_, c_]],
            dtype=np.float32)
        offset = body_offset - origin_offset - rotation@center_offset
        result = pyg.transform.rotate(
            self.tank_turret_textures[player], angle=180 * angle / np.pi)
        return (result, offset)

    def get_tank(self,
                 tank_player: int = 0,
                 tank_type: int = 0,
                 dir: int = 0,) -> pyg.Rect:
        # player = 0: user 0
        # player = 1: user 1
        # player = 2: strong ai
        # player = 3: weak ai
        player_offset = np.array(
            [tank_player // 2, tank_player % 2], dtype=np.int32)
        player_offset *= 128
        type_offset = np.array(
            [tank_player // 2, tank_player % 2], dtype=np.int32)

        return pyg.Rect(player_offset[0], player_offset[1], 15, 15)

    def get_block(self,
                  block_type: int = 0,
                  damage_type: int = 0) -> pyg.Surface:
        block_type = block_type % 4
        return self.block_textures[block_type]
