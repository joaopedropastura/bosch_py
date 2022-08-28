import pygame

backGroundColor = (255, 255, 55)
screen = pygame.display.set_mode((800,800))
pygame.display.set_caption('game by joaopedro')
backGroundImg = pygame.image.load("pac-man/sprites/Grass.png")
wallImg = pygame.image.load("pac-man/sprites/arbusto.png")
playerImg = pygame.image.load("pac-man/sprites/player_f1.png")
map = []

def make_matriz_mapa():
	for column in range(25):
		aux = []
		for line in range(25):
			aux.append("")
		map.append(aux)

def draw_backGround(map):
	for column in range(len(map)):
		for line in range(len(map)):
			map[column][line] = screen.blit(backGroundImg, (line*32,column*32))

def draw_wall(map):
	for column in range(len(map)):
		for line in range(len(map)):
			if column == 0 or column == len(map) - 1 or line == 0 or line == len(map)-1:
				map[column][line] = screen.blit(wallImg, (line*32,column*32))

def draw_player(map, x , y):
	map[x][y] = screen.blit(playerImg, (x*32,y*32))

def start_game(map):
	running = 1
	x = 1
	while running:
		for event in pygame.event.get():
			if event.type == pygame.KEYDOWN:
				x += 1
				draw_player(map, 1, x)
			if event.type == pygame.QUIT:
				running = 0
		pygame.display.update()

make_matriz_mapa()
draw_backGround(map)
draw_player(map, 1, 1)
draw_wall(map)
start_game(map)
