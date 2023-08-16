from core.constants import *


class UserInput:
    def __init__(self, player: int = 0) -> None:
        self.player = player
        # right, up, left, down
        self.dir_key_states = [False, False, False, False]
        self.fire_key_state = False
        self.dir = 0

    def handle_dir_key_events(self, dir_key_events: list[pyg.event]):
        if len(dir_key_events) == 0:
            return
        dir_changed = False
        # first deal with those key that is released
        for dir_key in dir_key_events:
            if dir_key.type == pyg.KEYUP:
                key_dir = PLAYER_DIRS[self.player].index(dir_key.key)
                self.dir_key_states[key_dir] = False
            # always use the latest down key to determine the direction
            elif dir_key.type == pyg.KEYDOWN:
                key_dir = PLAYER_DIRS[self.player].index(dir_key.key)
                self.dir_key_states[key_dir] = True
                self.dir = key_dir
                dir_changed = True
        # if there is no key down events and the are still keys being pressed, the first one is used
        if dir_changed == False:
            if True in self.dir_key_states:
                self.dir = self.dir_key_states.index(True)
