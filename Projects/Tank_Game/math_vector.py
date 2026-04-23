import pyray as pr


def vec_calc(start: pr.Vector2, current_v: pr.Vector2, rotation_speed : float, length: int, target: pr.Vector2 = None, end: pr.Vector2 = None):
    if end is not None:
        diff = pr.vector2_subtract(end, start)
        target = pr.vector2_normalize(diff)

    updated_v = pr.vector2_lerp(current_v, target, rotation_speed)
    updated_v = pr.vector2_normalize(updated_v)
    end_p = pr.vector2_add(start, pr.vector2_scale(updated_v, length))

    return end_p, updated_v


def render_math(unit_vector: pr.Vector2, center: pr.Vector2, turret_rad: float) -> tuple:
    side_offset = pr.vector2_scale(pr.Vector2(-unit_vector.y, unit_vector.x), (turret_rad * 2.5) / 2)
    forward_offset = pr.vector2_scale(unit_vector, (turret_rad * 4) / 2)
    
    p1 = pr.vector2_add(center, pr.vector2_add(forward_offset, side_offset))# Вперед-Вправо

    p2 = pr.vector2_subtract(pr.vector2_add(center, forward_offset), side_offset)# Вперед-Влево

    p3 = pr.vector2_subtract(center, pr.vector2_add(forward_offset, side_offset))# Назад-Влево
    
    p4 = pr.vector2_add(pr.vector2_subtract(center, forward_offset), side_offset)# Назад-Вправо

    return (p1, p2, p3, p4)
