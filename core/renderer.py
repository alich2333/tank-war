from core.texture_loader import *
from core.map import *
from core.game import *


class Renderer:
    def __init__(self,
                 texture_loader: TextureLoader,
                 map: Map,
                 game: Game) -> None:
        self.texture_loader = texture_loader
        self.map = map
        self.game = game

    def render_bricks(self):
        pass

    def render_player_tanks(self):
        for player in range(self.game.player_num):
            tank = self.game.player_tanks[player]
            dir = tank.get_dir()
            pos = tank.get_pos()
            pos = (int(pos[0]), int(pos[1]))
            angle = tank.get_angle()
            self.game.window.blit(
                self.texture_loader.get_player_tank_body_texture(player, dir),
                dest=pos)
            tex, offset = self.texture_loader.get_player_tank_turret_texture_and_offset(
                player, angle)
            self.game.window.blit(tex,
                                  dest=(pos[0] + offset[0], pos[1] + offset[1]))

    def render_ai_tanks(self):
        pass

    def render(self):
        self.render_bricks()
        self.render_player_tanks()
        self.render_ai_tanks()
