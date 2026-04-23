import pyray as pr

def render_tank(
    points_for_rect: tuple,
    end_for_barrel: pr.Vector2,
    center: pr.Vector2,
    tank_turret_r: float
):
    p1, p2, p3, p4 = points_for_rect

    pr.draw_triangle_fan([p1, p2, p3, p4], 4, pr.DARKBLUE)
    pr.draw_line_ex(center, end_for_barrel, 5.0, pr.BLACK)
    pr.draw_circle_v(center, tank_turret_r, pr.GRAY)
