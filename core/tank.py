from core.game_object import *


class Tank(GameObject):
    '''
    User and AI Tanks
    '''

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
                         pos=pos,
                         angle=0.5*math.pi*dir,
                         rotate_speed=0)
        self.turret = GameObject(is_dynamic=True,
                                 lives=init_lives,
                                 max_hp=init_max_hp,
                                 pos=pos,
                                 angle=0.5*math.pi*dir)

    def get_dir(self):
        return int(round(self.angle / (0.5*math.pi)))

    def get_pos(self):
        return self.pos

    def get_angle(self):
        return self.turret.angle

    def set_dir(self, dir: int = 0):
        dir = dir % 4
        self.angle = 0.5*math.pi*dir

    def set_speed(self, speed: tuple[float, float] = (0, 0)):
        self.speed = speed

    def set_turret_rotate_speed(self, rotate_speed: float = 0):
        self.rotate_speed = rotate_speed

    def move(self):
        self.turret.move()
        self.pos = (self.pos[0] + self.speed[0], self.pos[1] + self.speed[1])
        self.angle += self.rotate_speed
        pi_2 = 2*math.pi
        self.angle -= pi_2 * math.floor(self.angle / pi_2)
