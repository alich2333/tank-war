from core.game import *
from core.texture_loader import *
from core.map import *
from core.renderer import *

game_map = Map()
game = Game(game_map, 2)
texture_loader = TextureLoader()
renderer = Renderer(texture_loader, game_map, game)


theta = np.pi
# theta = 0


def test_ai_tank_rendering():
    game.window.blit(texture_loader.get_main_texture(),
                     dest=(0, 0),
                     area=texture_loader.get_tank(0))
    game.window.blit(texture_loader.get_main_texture(),
                     dest=(20, 0),
                     area=texture_loader.get_tank(1))
    game.window.blit(texture_loader.get_main_texture(),
                     dest=(40, 0),
                     area=texture_loader.get_tank(2))
    game.window.blit(texture_loader.get_main_texture(),
                     dest=(60, 0),
                     area=texture_loader.get_tank(3))


def test_player_tank_rendering():
    global theta
    theta = theta + 0.05
    if theta > 2 * np.pi:
        theta -= 2 * np.pi
    ofst = 80
    game.window.blit(texture_loader.get_player_tank_body_texture(0),
                     dest=(ofst*1, 100))
    game.window.blit(texture_loader.get_player_tank_body_texture(0),
                     dest=(ofst*2, 100))
    game.window.blit(texture_loader.get_player_tank_body_texture(0),
                     dest=(ofst*3, 100))
    game.window.blit(texture_loader.get_player_tank_body_texture(0),
                     dest=(ofst*4, 100))
    tex, offset = texture_loader.get_player_tank_turret_texture_and_offset(
        0, 0 + theta)
    game.window.blit(tex,
                     dest=(ofst*1 + offset[0], 100 + offset[1]))
    tex, offset = texture_loader.get_player_tank_turret_texture_and_offset(
        0, 0.5 * np.pi - theta)
    game.window.blit(tex,
                     dest=(ofst*2 + offset[0], 100 + offset[1]))
    tex, offset = texture_loader.get_player_tank_turret_texture_and_offset(
        0, 1 * np.pi + theta)
    game.window.blit(tex,
                     dest=(ofst*3 + offset[0], 100 + offset[1]))
    tex, offset = texture_loader.get_player_tank_turret_texture_and_offset(
        0, 1.5 * np.pi - theta)
    game.window.blit(tex,
                     dest=(ofst*4 + offset[0], 100 + offset[1]))

    game.window.blit(texture_loader.get_player_tank_body_texture(1),
                     dest=(ofst*1, 200))
    game.window.blit(texture_loader.get_player_tank_body_texture(1),
                     dest=(ofst*2, 200))
    game.window.blit(texture_loader.get_player_tank_body_texture(1),
                     dest=(ofst*3, 200))
    game.window.blit(texture_loader.get_player_tank_body_texture(1),
                     dest=(ofst*4, 200))
    tex, offset = texture_loader.get_player_tank_turret_texture_and_offset(
        1, 0 + theta)
    game.window.blit(tex,
                     dest=(ofst*1 + offset[0], 200 + offset[1]))
    tex, offset = texture_loader.get_player_tank_turret_texture_and_offset(
        1, 0.5 * np.pi - theta)
    game.window.blit(tex,
                     dest=(ofst*2 + offset[0], 200 + offset[1]))
    tex, offset = texture_loader.get_player_tank_turret_texture_and_offset(
        1, 1 * np.pi + theta)
    game.window.blit(tex,
                     dest=(ofst*3 + offset[0], 200 + offset[1]))
    tex, offset = texture_loader.get_player_tank_turret_texture_and_offset(
        1, 1.5 * np.pi - theta)
    game.window.blit(tex,
                     dest=(ofst*4 + offset[0], 200 + offset[1]))


def test_block_rendering():
    game.window.blit(texture_loader.get_block(0), (100, 400))
    game.window.blit(texture_loader.get_block(1), (200, 400))
    game.window.blit(texture_loader.get_block(2), (300, 400))
    game.window.blit(texture_loader.get_block(3), (400, 400))

while game.is_running:
    # I. Logical Frame
    # A. update with user inputs
    events = game.poll_events()

    # B. deal with events to set speed and rotate speed
    # 1. resolve user inputs
    game.resolve_events(events)
    # 2. update user tank states: dir, turret rotation, fire, skills
    game.set_user_tank_states()
    # 3. game menu
    # 4. map editor operations

    # C. move existing bullets and tanks
    # D. create new bullets and use user tank skills
    # E. get collision events (bullets with everything else)
    # F. update tanks' states, map, and bullets
    game.move_tanks()

    # II. Rendering Frame
    game.frame_begin()
    test_ai_tank_rendering()
    test_player_tank_rendering()
    test_block_rendering()
    renderer.render()
    game.frame_end()
