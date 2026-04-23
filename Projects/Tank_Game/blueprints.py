import pyray as pr
from dataclasses import dataclass



@dataclass
class Tank:
    center: pr.Vector2
    tank_vector: pr.Vector2
    barrel_vector: pr.Vector2
    barrel_end: pr.Vector2
    velocity: float = 40.0
    rotation_speed: float = 2.0
    turret_rad: float = 20.0
    barrel_length: int = 40
