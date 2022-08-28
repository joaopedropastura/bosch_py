from curses import KEY_DOWN
from platform import python_branch
import pygame
import random

WIDTH = 800
HEIGHT = 800

backGroundColor = (255, 255, 55)
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('game by github: @jpsoares01')
backGroundImg = pygame.image.load("2d-game/sprites/Grass.png").convert_alpha()
backGround = pygame.transform.scale(backGroundImg, [WIDTH, HEIGHT])
wallImg = pygame.image.load("2d-game/sprites/arbusto.png").convert_alpha()
playerImg = pygame.image.load("2d-game/sprites/player_f1.png").convert_alpha()
exitImg = pygame.image.load("2d-game/sprites/exit_1.png").convert_alpha()
collectableImg = pygame.image.load("2d-game/sprites/coletavel.png").convert_alpha()
exitOpenImg = pygame.image.load("2d-game/sprites/exit-open.png").convert_alpha()
clock = pygame.time.Clock()
map = []

class player_posicao():
	def __init__(self):
		self.player_x = 1
		self.player_y = 1
		self.collectable = 0
		pass

game = player_posicao()

def make_matriz_mapa():
	for column in range(25):
		aux = []
		for line in range(25):
			aux.append("")
		map.append(aux)

def draw_backGround(map):
	for column in range(len(map)):
		for line in range(len(map)):
			map[column][line] = 0
			screen.blit(backGroundImg, (line*32,column*32))

def draw_wall(map):
	for column in range(len(map)):
		for line in range(len(map)):
			if map[column][line] == 0:
				aux = random.randrange(1, 6)
				if aux == 5:
					map[column][line] = 1
					screen.blit(wallImg, (column*32,line*32))
			if column == 0 or column == len(map) - 1 or line == 0 or line == len(map)-1:
				map[column][line] = 1
				screen.blit(wallImg, (line*32,column*32))

def draw_player():
	screen.blit(playerImg, (game.player_x*32,game.player_y*32))

def draw_collectable(map):
	for column in range(2,len(map)):
		for line in range(2,len(map)):
			if map[column][line] == 0:
				aux = random.randrange(1, 100)
				if aux == 5:
					map[column][line] = 'C'
					game.collectable += 1
					screen.blit(collectableImg, (column*32,line*32))

def draw_exit():
	map[len(map)-2][len(map)-2] = 'E'
	screen.blit(exitImg, ((len(map)-2)*32,(len(map)-2)*32))

def draw_game():
	draw_backGround(map)
	draw_wall(map)

def check_step(map, code):
	if game.collectable > 0:
		if code == pygame.K_DOWN:
			if map[game.player_x][game.player_y + 1] != 1 and map[game.player_x][game.player_y + 1] != 'E':
				screen.blit(backGroundImg, (game.player_x*32,game.player_y*32))
				game.player_y += 1
		if code == pygame.K_UP:
			if map[game.player_x][game.player_y - 1] != 1 and map[game.player_x][game.player_y - 1] != 'E':
				screen.blit(backGroundImg, (game.player_x*32,game.player_y*32))
				game.player_y -= 1
		if code == pygame.K_RIGHT:
			if map[game.player_x + 1][game.player_y] != 1 and map[game.player_x + 1][game.player_y] != 'E':
				screen.blit(backGroundImg, (game.player_x*32,game.player_y*32))
				game.player_x += 1
		if code == pygame.K_LEFT:
			if map[game.player_x - 1][game.player_y] != 1 and map[game.player_x - 1][game.player_y] != 'E':
				screen.blit(backGroundImg, (game.player_x*32,game.player_y*32))
				game.player_x -= 1
		check_collectable()
	else:
		open_exit(code)
		screen.blit(exitOpenImg, ((len(map)-2)*32,(len(map)-2)*32))

def check_collectable():
	print(game.collectable)
	if map[game.player_x][game.player_y] == 'C':
		map[game.player_x][game.player_y] = 0
		game.collectable -= 1

def open_exit(code):
	if code == pygame.K_DOWN:
		if map[game.player_x][game.player_y + 1] != 1:
			screen.blit(backGroundImg, (game.player_x*32,game.player_y*32))
			game.player_y += 1
	if code == pygame.K_UP:
		if map[game.player_x][game.player_y - 1] != 1:
			screen.blit(backGroundImg, (game.player_x*32,game.player_y*32))
			game.player_y -= 1
	if code == pygame.K_RIGHT:
		if map[game.player_x + 1][game.player_y] != 1:
			screen.blit(backGroundImg, (game.player_x*32,game.player_y*32))
			game.player_x += 1
	if code == pygame.K_LEFT:
		if map[game.player_x - 1][game.player_y] != 1:
			screen.blit(backGroundImg, (game.player_x*32,game.player_y*32))
			game.player_x -= 1


def game_loop(map):
	running = 1
	while running:
		clock.tick(30)
		# screen.blit(backGround, (0, 0))
		for event in pygame.event.get():
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_DOWN:
					check_step(map, pygame.K_DOWN)
				if event.key == pygame.K_UP:
					check_step(map, pygame.K_UP)
				if event.key == pygame.K_RIGHT:
					check_step(map, pygame.K_RIGHT)
				if event.key == pygame.K_LEFT:
					check_step(map, pygame.K_LEFT)
				draw_player()
			if event.type == pygame.QUIT or map[game.player_x][game.player_y] == 'E':
				running = 0
		pygame.display.flip()
	pygame.display.update()

make_matriz_mapa()
draw_game()
draw_player()
draw_collectable(map)
draw_exit()
game_loop(map)
