import pygame as pyg
import math


class GameObject:
    '''
        base class for all dynamic and static objects such as tank, bullet and bricks
    '''

    def __init__(self,
                 is_dynamic: bool = False,
                 lives: int = 1,
                 max_hp: float = 100,
                 proactive_damage: float = 0,
                 passive_damage: float = 0,
                 pos: tuple[float, float] = (0, 0),
                 speed: tuple[float, float] = (0, 0),
                 angle: float = 0,# in rad
                 rotate_speed: float = 0) -> None:
        # life states
        self.max_hp = max_hp
        self.lives = lives
        self.hp = max_hp
        self.is_dynamic = is_dynamic
        self.should_rebirth = False
        self.should_die = False
        # attack states
        self.proactive_damage = proactive_damage
        self.passive_damage = passive_damage
        # physical states
        self.pos = pos
        self.angle = angle
        self.speed = speed
        self.rotate_speed = rotate_speed

    def get_hit(self, damage: float):
        if self.hp == 0 or damage <= 0:
            return
        self.hp -= damage
        if self.hp < 0:
            self.hp = 0
            self.lives -= 1
            if self.lives == 0:
                self.should_die = True

    def is_alive(self):
        return self.hp > 0

    def move(self):
        self.pos += self.speed
        self.angle += self.rotate_speed
        pi_2 = 2*math.pi
        self.angle -= pi_2 * math.floor(self.angle / pi_2)


def hit(proa_obj: GameObject, pass_obj: GameObject):
    if not (proa_obj.is_alive() and pass_obj.is_alive()):
        return
    pass_obj.get_hit(proa_obj.proactive_damage)
    proa_obj.get_hit(proa_obj.passive_damage)
