from pyray import *

height = 500
width = 500


class Ball:
	def __init__(self, size: (int, float), pos: Vector2, speed: Vector2, ball_color: Color, sound):

		is_size_ok = isinstance(size, (int, float))
		is_pos_ok = hasattr(pos, 'x') and hasattr(pos, 'y')
		is_speed_ok = hasattr(speed, 'x') and hasattr(speed, 'y')
		is_color_ok = hasattr(ball_color, 'r') or (isinstance(ball_color, (list, tuple)) and len(ball_color) >= 3)

		if not (is_size_ok and is_pos_ok and is_speed_ok and is_color_ok):
			import sys
			print(f"""
				size_status -> {is_size_ok}
				pos_status -> {is_pos_ok}
				speed_status -> {is_speed_ok}
				color_status -> {is_color_ok} 
				""")
			sys.exit(1)

		self.size = size
		self.pos = pos
		self.speed = speed
		self.ball_color = ball_color
		self.sound = sound

	def draw_ball(self):
		draw_circle_v(self.pos, self.size, self.ball_color)

	def control(self):
		if is_key_down(KEY_RIGHT): self.pos.x += 5

		if is_key_down(KEY_LEFT): self.pos.x -= 5

		if is_key_down(KEY_UP): self.pos.y -= 5

		if is_key_down(KEY_DOWN): self.pos.y += 5

	def wall_bounce(self):
		if self.pos.x < self.size:

			self.pos.x = self.size
			self.speed.x *= -1
			play_sound(self.sound)


		if self.pos.x > get_screen_width() - self.size:

			self.pos.x = get_screen_width() - self.size
			self.speed.x *= -1
			play_sound(self.sound)

		if self.pos.y < self.size:

			self.pos.y = self.size
			self.speed.y *= -1
			play_sound(self.sound)

		if self.pos.y > get_screen_height() - self.size:

			self.pos.y = get_screen_height() - self.size
			self.speed.y *= -1
			play_sound(self.sound)

	def start(self):
		self.pos.x += self.speed.x
		self.pos.y += self.speed.y



			 





#-------------------------------------------------------------|
#-------------------------------------------------------------|	

init_window(height, width, "It's working!!!!!!!")

init_audio_device()

bounce_sound = load_sound("Pickup4.wav")
set_target_fps(60)

font = load_font_ex("arial.ttf", 64, None, 0)
set_texture_filter(font.texture, TEXTURE_FILTER_BILINEAR)

ball = Ball(20, Vector2(250, 250), Vector2(4, 3), GRAY, bounce_sound)

while not window_should_close():

	begin_drawing()
	clear_background(SKYBLUE)

	ball.draw_ball()
	ball.control()
	draw_text_ex(font, "It's result of my half-baked code\n:)", Vector2(10, 10), 20, 2, BLACK)

	end_drawing()
unload_sound(bounce_sound)
close_audio_device()
unload_font(font)
close_window()