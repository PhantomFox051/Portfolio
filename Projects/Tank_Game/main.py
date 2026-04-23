import pyray as pr
from tank_logic import TankSystem
from blueprints import Tank
from math_vector import render_math
from render import render_tank

def main():
    first_tank = Tank(
        center = pr.Vector2(500, 500),
        tank_vector = pr.Vector2(0, -1),
        barrel_vector = pr.Vector2(0, -1),
        barrel_end = pr.Vector2(500, 460)
    )
    first_tank_system = TankSystem(tank = first_tank)

    pr.init_window(1000, 1000, "TANK_GAME")
    pr.set_target_fps(60)

    while not pr.window_should_close():

        first_tank_system.control_tank()
        first_tank_system.control_barrel()
        render_points = render_math(first_tank.tank_vector, first_tank.center, first_tank.turret_rad)
        pr.begin_drawing()
        pr.clear_background(pr.RAYWHITE)
        render_tank(render_points, first_tank.barrel_end, first_tank.center, first_tank.turret_rad)
        pr.end_drawing()
    pr.close_window()
if __name__ == '__main__':
    main()
