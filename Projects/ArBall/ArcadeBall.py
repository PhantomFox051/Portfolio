import arcade as ar
print("IT'S WORKING!!!!!!!!")


class ArBall(ar.Window):

	def __init__(self):

		super().__init__(500, 500, "IT'S WORKING!!!!!!!!")

		ar.set_background_color(ar.color.WHITE)

		self.ball = ar.SpriteCircle(15, ar.color.BLACK)

		self.user_ball = ar.SpriteCircle(15, ar.color.GRAY)

		self.ball.center_x = 250
		self.ball.center_y = 250

		self.ball.change_x = 4
		self.ball.change_y = 5

		self.user_ball.change_x = 0
		self.user_ball.change_y = 0

		self.user_ball.center_x = 125
		self.user_ball.center_y = 125

		self.ball_list = ar.SpriteList()
		self.ball_list.append(self.ball)
		self.ball_list.append(self.user_ball)
		self.sound = ar.load_sound("Pickup4.wav")


	def on_draw(self):

		self.clear()

		self.ball_list.draw()

	def on_update(self, delta_time):

		self.ball_list.update()

		self.control()

		self.check_wall_collision()



	def check_wall_collision(self):

		for ball in self.ball_list:
			if ball.left < 0: 
				ball.left = 0

			if ball.right > self.width: 
				ball.right = self.width	

			if ball.bottom < 0: 
				ball.bottom = 0

			if ball.top > self.height: 
				ball.top = self.height

	def control(self):

		if self.keyboard[ar.key.RIGHT]: 
			self.user_ball.change_x = 5

		elif self.keyboard[ar.key.LEFT]: 
			self.user_ball.change_x = -5

		else: 
			self.user_ball.change_x = 0

		
		if self.keyboard[ar.key.DOWN]: 
			self.user_ball.change_y = -5

		elif self.keyboard[ar.key.UP]: 
			self.user_ball.change_y = 5

		else: 
			self.user_ball.change_y = 0







if __name__ == '__main__':
	game = ArBall()
	ar.run()