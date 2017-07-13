import pygame
import time

SIZE = (640, 480)
BLACK = (0, 0 ,0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
GREY = (128, 128, 128)
YELLOW = (255, 255, 0)
Color = [BLACK, WHITE, RED, GREEN, BLUE, GREY, YELLOW]
pygame.init()
screen = pygame.display.set_mode(SIZE)
pygame.display.set_caption("Hello World!")
x = 0
y = 0
square = pygame.Rect(640/2 - 100/2, 480/2 - 100/2, 100, 100)
direction = 1

while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			exit()
		elif event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT:
			direction *= 2
		elif event.type == pygame.KEYDOWN and event.key == pygame.K_LEFT:
			direction /= 2
		elif event.type == pygame.KEYDOWN and event.key == pygame.K_UP:
			x += 1
			if x > 6:
				x = 0
		elif event.type == pygame.KEYDOWN and event.key == pygame.K_DOWN:
			y += 1
			if y > 6:
				y = 0
		elif event.type == pygame.KEYDOWN and event.key == pygame.K_w:
			square.w += 10
			square.h += 10
		elif event.type == pygame.KEYDOWN and event.key == pygame.K_s:
			square.w -= 10
			square.h -= 10
	screen.fill(Color[y])
	pygame.draw.rect(screen, Color[x], square)
	pygame.display.flip()

	time.sleep(1/30)

	square = square.move(direction, 0)
	if square.x + square.w >= SIZE[0]:
		direction = -abs(direction)
	elif square.x <= 0:
		direction = abs(direction)
