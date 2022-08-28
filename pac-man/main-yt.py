import pygame

WIDTH = 900
HEIGHT = 600

pygame.init()
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("joaozinho")

gameLoop = True
while gameLoop:
	pygame.display.update()
