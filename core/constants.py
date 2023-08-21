# config file
import pygame as pyg

PLAYER_LIVES = 3
PLAYER_MAX_HP = 200
BLOCK_LENGTH = 60
MAP_WIDTH = 13
MAP_HEIGHT = 13
TURRET_SCALE = 0.95
TANK_SPEED = 3.0
BRICK_NUM = 20

# brick lives and hps
BRICK_LIVES = 16
BRICK_HP = 50
STEEL_BRICK_LIVES = 16
STEEL_BRICK_HP = 200

# base
BASE_LIVES = 1
BASE_HP = 500

# block types
SPAWN_POINT_BLOCK = -1 # spawn point (no rendering)
EMPYT_BLOCK = 0 #  empty (no rendering)
BRICK_BLOCK = 1 #  brick
STEEL_BRICK_BLOCK = 2 #  steel brick
BUSH_BLOCK = 3 #  bush
WATER_BLOCK = 4 #  water
BASE_BLOCK = 5 #  base
DESTORYED_BASE_BLOCK = 6 #  destroyed base

# baes position
PLAYER_BASE = [0, MAP_HEIGHT - 1]
AI_BASE = [MAP_WIDTH - 1, 0]

PLAYER_BASE_BRICKS = [[0,MAP_HEIGHT - 2], [1,MAP_HEIGHT - 2], [1,MAP_HEIGHT - 1]]
AI_BASE_BRICKS = [[MAP_WIDTH - 2,0], [MAP_WIDTH - 2,1], [MAP_WIDTH - 1,1]]

# respawn point
PLAYER_SPAWN_POINTS = [[0 , MAP_HEIGHT - 3], [2, MAP_HEIGHT - 1]]
AI_SPAWN_POINTS = [[MAP_WIDTH - 3, 0], [MAP_WIDTH - 1, 2]]

SPEED_CONSTANTS = [(TANK_SPEED, 0), (0, -TANK_SPEED),
                   (-TANK_SPEED, 0), (0, TANK_SPEED)]
# player inputs
PLAYER_DIRS = [[pyg.K_d, pyg.K_w, pyg.K_a, pyg.K_s],
               [pyg.K_RIGHT, pyg.K_UP, pyg.K_LEFT, pyg.K_DOWN]]
PLAYER_FIRE = [pyg.K_SPACE, pyg.K_KP_ENTER]
# turret control engagement
