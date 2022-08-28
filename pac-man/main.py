from curses import KEY_DOWN
from platform import python_branch
import pygame

WIDTH = 800
HEIGHT = 800

backGroundColor = (255, 255, 55)
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('game by github: @jpsoares01')
backGroundImg = pygame.image.load("2d-game/sprites/Grass.png")
backGround = pygame.transform.scale(backGroundImg, [WIDTH, HEIGHT])
wallImg = pygame.image.load("2d-game/sprites/arbusto.png")
playerImg = pygame.image.load("2d-game/sprites/player_f1.png")
exitImg = pygame.image.load("2d-game/sprites/exit_1.png")
clock = pygame.time.Clock()
map = []

class player_posicao():
	def __init__(self):
		self.player_x = 1
		self.player_y = 1
		pass

player = player_posicao()

class player_img(pygame.sprite.Sprite):
	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.image.load("2d-game/sprites/player_f1.png")
		self.rect = pygame.Rect(32, 32, 32, 32)

	def update(self, *args):
		self.image = pygame.transform.scale(self.image, [32,32])

playerGroup = pygame.sprite.Group()
player = player_img()
playerGroup.add(player)

def make_matriz_mapa():
	for column in range(25):
		aux = []
		for line in range(25):
			aux.append("")
		map.append(aux)


def draw():
	playerGroup.draw(screen)

def update():
	playerGroup.update()

def draw_backGround(map):
	screen.fill(backGroundColor)
	for column in range(len(map)):
		for line in range(len(map)):
			map[column][line] = screen.blit(backGroundImg, (line*32,column*32))

def draw_wall(map):
	for column in range(len(map)):
		for line in range(len(map)):
			if column == 0 or column == len(map) - 1 or line == 0 or line == len(map)-1:
				map[column][line] = screen.blit(wallImg, (line*32,column*32))

def draw_player(map, x , y):
	# draw_game()
	map[x][y] = screen.blit(update, (x*32,y*32))

def draw_game():
	# draw_backGround(map)
	draw_wall(map)

def check_step(map, code):
	player = player_posicao()
	if code == pygame.K_DOWN and map[player.player_x][player.player_y + 1] != wallImg:
		player.player_y += 1
		draw_player(map, player.player_x, player.player_y)


def game_loop(map):
	player = player_posicao()
	running = 1
	while running:
		clock.tick(30)
		screen.blit(backGround, (0, 0))
		for event in pygame.event.get():
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_DOWN:
					check_step(map, pygame.K_DOWN)
				if event.key == pygame.K_UP:
					player.player_y -= 1
					draw_player(map, player.player_x, player.player_y)
				if event.key == pygame.K_RIGHT:
					player.player_x += 1
					draw_player(map, player.player_x, player.player_y)
				if event.key == pygame.K_LEFT:
					player.player_x -= 1
					draw_player(map, player.player_x, player.player_y)
			pygame.display.update()
			if event.type == pygame.QUIT:
				running = 0
		update()
		draw()
		pygame.display.update()

make_matriz_mapa()
draw_game()
draw_player(map, player.player_x, player.player_y)
game_loop(map)

