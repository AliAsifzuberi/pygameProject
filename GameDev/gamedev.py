# pygame template - skeleton for a new pygame project
import pygame
import random

WIDTH = 360 # width of our game window 
HEIGHT = 480 # heieght of our game window 
FPS = 30

pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("My Game")
clock = pygame.time.Clock()
#screen.fill(BLACK)

running = True

while running:
	clock.tick(FPS)
