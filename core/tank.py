from core.game_object import *


class Tank(GameObject):
    def __init__(self,
                 init_lives: int = 3,
                 init_max_hp: float = 100,
                 pos: tuple[float, float] = (0, 0),
                 dir: int = 0) -> None:
        dir = dir % 4
        super().__init__(is_dynamic=True,
                         lives=init_lives,
                         max_hp=init_max_hp,
                         proactive_damage=0,  # since we attack with bullets
                         passive_damage=0,
                         pos=pos,
                         angle=0.5*math.pi*dir,
                         rotate_speed=0)
