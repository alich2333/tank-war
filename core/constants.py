import pygame as pyg

PLAYER_LIVES = 3
PLAYER_MAX_HP = 200
BLOCK_LENGTH = 60
MAP_WIDTH = 15
MAP_HEIGHT = 15
TURRET_SCALE = 0.95
TANK_SPEED = 3.0

SPEED_CONSTANTS = [(TANK_SPEED, 0), (0, -TANK_SPEED),
                   (-TANK_SPEED, 0), (0, TANK_SPEED)]
# player inputs
PLAYER_DIRS = [[pyg.K_d, pyg.K_w, pyg.K_a, pyg.K_s],
               [pyg.K_RIGHT, pyg.K_UP, pyg.K_LEFT, pyg.K_DOWN]]
PLAYER_FIRE = [pyg.K_SPACE, pyg.K_KP_ENTER]
# turret control engagement
