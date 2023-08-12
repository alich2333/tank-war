from core.game import *
from core.texture_loader import *
from core.map import *

map = Map()
game = Game(map.get_map_sizes_in_pixel())
texture_loader = TextureLoader()

while game.is_running:
    game.poll_events()
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
