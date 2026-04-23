import pyray as pr
from blueprints import Tank
from math_vector import vec_calc

class TankSystem:
    def __init__(self, tank: Tank):
        self.tank = tank

    def control_barrel(self):
        dt = pr.get_frame_time()
        mouse = pr.get_mouse_position()

        self.tank.barrel_end, self.tank.barrel_vector = vec_calc(
            self.tank.center,
            self.tank.barrel_vector,
            self.tank.rotation_speed * dt,
            self.tank.barrel_length,
            end = mouse
        )



    def control_tank(self):
        dt = pr.get_frame_time()


        if pr.is_key_down(pr.KEY_W):
            self.tank.center = pr.vector2_add(self.tank.center, pr.vector2_scale(self.tank.tank_vector, self.tank.velocity * dt))


        elif pr.is_key_down(pr.KEY_S):
            self.tank.center = pr.vector2_subtract(self.tank.center, pr.vector2_scale(self.tank.tank_vector, self.tank.velocity * dt))



        if pr.is_key_down(pr.KEY_A):
            _, self.tank.tank_vector = vec_calc(
                self.tank.center,
                self.tank.tank_vector,
                self.tank.rotation_speed * dt,
                self.tank.barrel_length,
                target = pr.Vector2(self.tank.tank_vector.y, -self.tank.tank_vector.x
                )
            )
        elif pr.is_key_down(pr.KEY_D):
            _, self.tank.tank_vector = vec_calc(
                self.tank.center,
                self.tank.tank_vector,
                self.tank.rotation_speed * dt,
                self.tank.barrel_length,
                target = pr.Vector2(-self.tank.tank_vector.y, self.tank.tank_vector.x)
            )
