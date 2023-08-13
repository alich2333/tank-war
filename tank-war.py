from core.game import *
from core.texture_loader import *
from core.map import *

map = Map()
game = Game(map.get_map_sizes_in_pixel())
texture_loader = TextureLoader()

while game.is_running:
    # I. Logical Frame
    # A. update with user inputs
    events = game.poll_events()

    # B. deal with events to set speed and rotate speed
    # 1. update user tank states: dir, turret rotation, fire, skills
    # 2. game menu
    # 3. map editor operations
    # game.update_with_events(events)

    # C. move existing bullets and tanks
    # D. create new bullets and use user tank skills
    # E. get collision events (bullets with everything else)
    # F. update tanks' states, map, and bullets

    # II. Rendering Frame
    game.frame_begin()
    game.window.blit(texture_loader.get_texture(),
                     dest=(100, 100),
                     area=pyg.Rect(0, 0, 15, 15))
    game.window.blit(texture_loader.get_texture(),
                     dest=(0, 0),
                     area=texture_loader.get_tank(0))
    game.window.blit(texture_loader.get_texture(),
                     dest=(20, 0),
                     area=texture_loader.get_tank(1))
    game.window.blit(texture_loader.get_texture(),
                     dest=(40, 0),
                     area=texture_loader.get_tank(2))
    game.window.blit(texture_loader.get_texture(),
                     dest=(60, 0),
                     area=texture_loader.get_tank(3))
    game.frame_end()
