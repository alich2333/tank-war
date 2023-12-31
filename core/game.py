import pygame as pyg

from core.constants import *
from core.tank import *
from core.map import *
from core.user_input import *


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
        self.ai_num = 0
        self.is_running = True
        self.should_quit = False

        # save tanks in a list
        self.player_tanks = [self.create_new_player_tank((PLAYER_SPAWN_POINTS[player][0] * BLOCK_LENGTH, PLAYER_SPAWN_POINTS[player][1] * BLOCK_LENGTH)) for player in range(player_num)]
        self.player_inputs = [UserInput(player)
                              for player in range(player_num)]
        self.ai_tanks = []

    def __del__(self):
        pyg.quit()

    def create_new_player_tank(self, pos: tuple[float, float]) -> Tank:
        return Tank(init_lives=PLAYER_LIVES,
                    init_max_hp=PLAYER_MAX_HP,
                    pos=pos,
                    dir=1)

    def respawn_tank(self, tank_player: int = 0):
        if len(self.player_tanks):
            self.player_tanks[tank_player] = Tank()

    def poll_events(self):
        events = pyg.event.get()
        for event in events:
            if event.type == pyg.QUIT:
                self.should_quit = True
            if event.type == pyg.KEYDOWN:
                if event.key == pyg.K_ESCAPE:
                    self.should_quit = True
        return events

    def resolve_events(self, events: list[pyg.event]):
        dir_key_events = [[] for player in range(self.player_num)]
        for event in events:
            # get player keys
            for player in range(self.player_num):
                if (event.type == pyg.KEYDOWN) or (event.type == pyg.KEYUP):
                    if event.key in PLAYER_DIRS[player]:
                        dir_key_events[player].append(event)
                    if event.key == PLAYER_FIRE[player]:
                        if event.type == pyg.KEYDOWN:
                            self.player_inputs[player].fire_key_state = True
                        elif event.type == pyg.KEYUP:
                            self.player_inputs[player].fire_key_state = False
        for player in range(self.player_num):
            self.player_inputs[player].handle_dir_key_events(
                dir_key_events[player])

    def set_player_tank_states(self):
        for player in range(self.player_num):
            player_input = self.player_inputs[player]
            player_tank = self.player_tanks[player]
            dir = player_input.dir
            player_tank.set_dir(dir)
            # print(player_input.dir_key_states)
            if player_input.dir_key_states[dir]:
                player_tank.set_speed(SPEED_CONSTANTS[dir])
            else:
                player_tank.set_speed((0, 0))

    def get_collision_events_and_move(self):
        # algorithm: optimize O(m * n)
        # get static obects
        # blocks and map edges
        static_object_rects = [wall.get_rect() for wall in self.map.wall_list]
        for i in range(4):
            static_object_rects.append(self.map.get_boundary_rect(i))
        map_edges_offset = len(self.map.wall_list)
        static_offset = len(static_object_rects)

        # get dynmaic obects
        # tanks and bullets
        dynamic_object_rects = [tank.get_future_rect() for tank in self.player_tanks] + [tank.get_future_rect() for tank in self.ai_tanks]
        tank_offset = len(dynamic_object_rects)
        # todo: add bullets
        dynamic_object_num = len(dynamic_object_rects)

        object_rects = static_object_rects + dynamic_object_rects
        collision_pairs = [] # tuples: (dynamic_obj_id, static or dynamic)
        for i in range(dynamic_object_num):
            dynamic_rect = dynamic_object_rects[i]
            # get all obects except for the one to collide with
            target_object_rects = static_object_rects + dynamic_object_rects[i + 1:]
            collisions = dynamic_rect.collidelistall(target_object_rects)
            for j in collisions:
                collision_idx = j
                if j >= static_offset:
                    collision_idx = j + i + 1
                collision_pairs.append((i, collision_idx))

        if len(collision_pairs):
            print([(object_rects[collision[0]], object_rects[collision[1]]) for collision in collision_pairs])

        # handle collision events:
        for collision in collision_pairs:
            dynamic_object_id = collision[0]
            hit_object_id = collision[1]
            # move tanks: judge whether the tank is colliding with static objects
            if dynamic_object_id < tank_offset and hit_object_id < static_offset:
                if dynamic_object_id < self.player_num:
                    self.player_tanks[dynamic_object_id].set_speed((0, 0))
                elif dynamic_object_id < self.player_num + self.ai_num:
                    self.ai_tanks[dynamic_object_id - self.player_num].set_speed((0, 0))
            # move bullets:
            # todo
        self.move_tanks()

    def move_tanks(self):
        for player in range(self.player_num):
            player_tank = self.player_tanks[player]
            player_tank.move()

    def frame_begin(self):
        self.window.fill("black")

    def frame_end(self):
        pyg.display.flip()
        self.clock.tick(60)
        if self.should_quit:
            self.is_running = False
