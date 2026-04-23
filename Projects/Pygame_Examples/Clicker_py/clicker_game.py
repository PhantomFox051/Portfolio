import pygame as pg
import random

pg.init()
screen = pg.display.set_mode((800, 600))
font = pg.font.Font(None, 36)
score = 0
run = True

random_x_circle = random.randint(25, 775)
random_y_circle = random.randint(25, 575)
speed = 0.1
while run:
	mouse_x, mouse_y = pg.mouse.get_pos()
	dist = ((mouse_x - random_x_circle)**2 + (mouse_y - random_y_circle)**2)**0.5
	for event in pg.event.get():
		if event.type == pg.QUIT:
			run = False
		if dist < 25 and event.type == pg.MOUSEBUTTONDOWN and event.button == 1:
			random_x_circle = random.randint(25, 775)

			random_y_circle = random.randint(25, 575)

			score += 1	

	text_surface = font.render(f"Score: {score}", True, (255, 255, 255))

	screen.fill((0, 0, 0))

	screen.blit(text_surface, (50, 50))

	pg.draw.circle(screen, (255,0,0), (random_x_circle, random_y_circle), 25)

	pg.display.flip()



pg.quit()