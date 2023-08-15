import pygame as pyg

from core.constants import *
from core.tank import *
from core.map import *


class Game:
    '''
    Main game class
    '''

    def __init__(self,
                 map: Map,
                 player_num: int = 1) -> None:
        pyg.init()
        if player_num < 1:
            player_num = 1
        if player_num > 2:
            player_num = 2
        window_size = map.get_map_sizes_in_pixel()
        self.map = map
        self.window = pyg.display.set_mode(window_size)
        self.clock = pyg.time.Clock()
        self.player_num = player_num
        self.is_running = True
        self.should_quit = False

        # save tanks in a list
        self.player_tanks = [self.create_new_player_tank(
            self.player_tank_inital_pos(player)) for player in range(player_num)]
        self.ai_tanks = []

    def __del__(self):
        pyg.quit()

    def create_new_player_tank(self, pos: tuple[float, float]) -> Tank:
        return Tank(init_lives=PLAYER_LIVES,
                    init_max_hp=PLAYER_MAX_HP,
                    pos=pos,
                    dir=1)

    def player_tank_inital_pos(self, player):
        map_width = self.map.width
        map_height = self.map.height
        pos = np.array(
            [BLOCK_LENGTH, BLOCK_LENGTH], dtype=np.float32)
        if player == 0:
            pos[0] *= 0
            pos[1] *= map_height - 3
        else:
            pos[0] *= 2
            pos[1] *= map_height - 1
        return (pos[0], pos[1])

    def respawn_tank(self, tank_player: int = 0):
        if len(self.player_tanks):
            self.player_tanks[tank_player] = Tank()
        pass

    def poll_events(self):
        events = pyg.event.get()
        for event in events:
            if event.type == pyg.QUIT:
                self.should_quit = True
            if event.type == pyg.KEYDOWN:
                if event.key == pyg.K_ESCAPE:
                    self.should_quit = True
        return events

    def update_with_events(self, events):
        pass

    def frame_begin(self):
        self.window.fill("black")

    def frame_end(self):
        pyg.display.flip()
        self.clock.tick(60)
        if self.should_quit:
            self.is_running = False
