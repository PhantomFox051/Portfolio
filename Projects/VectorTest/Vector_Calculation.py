import pyray as pr

def VectorLineCalculation(start: pr.Vector2, end: pr.Vector2, rotation_speed : float, current_v: pr.Vector2, length: int):

    diff = pr.vector2_subtract(end, start)
    target = pr.vector2_normalize(diff)

    updated_v = pr.vector2_lerp(current_v, target, rotation_speed)
    updated_v = pr.vector2_normalize(updated_v)

    end_p = pr.vector2_add(start, pr.vector2_scale(updated_v, length))

    return end_p, updated_v




pr.init_window(500, 500, "It's working!!!!!!!")
pr.set_target_fps(60)

current_vector = pr.Vector2(1, 0)
pos = pr.Vector2(250, 250)
target_pos = pr.Vector2(250, 250)
speed = 2

while not pr.window_should_close():
    if pr.is_mouse_button_down(pr.MOUSE_BUTTON_LEFT):
        target_pos = pr.get_mouse_position()

    end_point, current_vector = VectorLineCalculation(pos, target_pos, speed * pr.get_frame_time(), current_vector, 60)




    pr.begin_drawing()
    pr.clear_background(pr.RAYWHITE)

    pr.draw_circle_v(pos, 20, pr.DARKGRAY)
    pr.draw_line_ex(pos, end_point, 15, pr.MAROON)
    pr.end_drawing()

pr.close_window()
