import pygame as pg

pg.init()

width, height = 800, 600
screen  = pg.display.set_mode((width, height))

clock = pg.time.Clock()
run = True

ball_x = width / 2
ball_y = height / 2
ball_radius = 20
ball_speedY, ball_speedX = 7, 7

while run:
	for event in pg.event.get():
		if event.type == pg.QUIT:
			run = False

	ball_x += ball_speedX
	ball_y += ball_speedY

	if ball_x < ball_radius:
		ball_x = ball_radius
		ball_speedX = -ball_speedX 
	elif ball_x > width - ball_radius:
		ball_x = width - ball_radius
		ball_speedX = -ball_speedX 


	if ball_y < ball_radius:
		ball_y = ball_radius
		ball_speedY = -ball_speedY
	elif ball_y > height - ball_radius:
		ball_y = height - ball_radius
		ball_speedY = -ball_speedY

		

	screen.fill((255, 255, 255))

	pg.draw.circle(screen, (0, 0, 0), (int(ball_x), int(ball_y)), ball_radius)

	pg.display.flip()
	clock.tick(60)

pg.quit()

