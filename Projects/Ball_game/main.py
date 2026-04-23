import arcade as ar
from ball_object import Ball
from json_reader import JsonReader

class BallGame(ar.Window):
	SOUND = ar.load_sound("Pickup4.wav")
	DATA = JsonReader("ball_config.json").load_json()

	def __init__(self):

		super().__init__(self.DATA["width"], self.DATA["height"], "It's result of my half-baked code")


		ar.set_background_color(ar.color.WHITE)

		self.ball_sprite = ar.SpriteCircle(self.DATA["radius"], ar.color.BLACK)

		self.ball_sprite.position = (self.get_size()[0] // 2, self.get_size()[1] // 2)

		self.ball = Ball(self.ball_sprite, self.get_size(), (self.DATA["change_x"], self.DATA["change_y"]))


		self.object_list = ar.SpriteList()
		self.object_list.append(self.ball_sprite)



	def on_draw(self):

		self.clear()

		self.object_list.draw()

	def on_update(self, delta_time):
		self.object_list.update()

		if self.ball.wall_bounce():
			ar.play_sound(self.SOUND)



if __name__ == '__main__':
	game = BallGame()
	ar.run()
