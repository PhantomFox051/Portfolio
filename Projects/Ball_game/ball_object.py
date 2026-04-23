import arcade as ar


class Ball:
	MIN_POS = 0
	def __init__(self, sprite_ball: ar.Sprite, screen_size: tuple[int, int], velocity: tuple[int, int]):
		self.sprite_ball = sprite_ball
		self.screen_size = screen_size
		self.sprite_ball.velocity = velocity		
		
	def check_collision(self):

		return {
		"collision_top": self.sprite_ball.top > self.screen_size[1],
		"collision_bottom": self.sprite_ball.bottom < self.MIN_POS,
		"collision_right": self.sprite_ball.right > self.screen_size[0],
		"collision_left": self.sprite_ball.left < self.MIN_POS
		}
		


	def wall_bounce(self):
		
		state_bounce = self.check_collision()
			
		if state_bounce["collision_top"]:
			self.sprite_ball.top = self.screen_size[1]
			self.sprite_ball.change_y *= -1

		elif state_bounce["collision_bottom"]:
			self.sprite_ball.bottom = self.MIN_POS
			self.sprite_ball.change_y *= -1

				
		if state_bounce["collision_right"]:
			self.sprite_ball.right = self.screen_size[0]
			self.sprite_ball.change_x *= -1
			
		elif state_bounce["collision_left"]:
			self.sprite_ball.left = self.MIN_POS
			self.sprite_ball.change_x *= -1

		return any(state_bounce.values())



