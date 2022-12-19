# Pygame template - skeleton for a new pygame project
import pygame
import random
import os # To get the directory path


WIDTH = 800 # Width of our game window 
HEIGHT = 600 # Heieght of our game window 
FPS = 30

#define colors
WHITE = (255,255,255)
BLACK = (0,0,0)
RED = (255,0,0)
BLUE = (0,0,255)
GREEN = (0,255,0)

class Player(pygame.sprite.Sprite):
	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
		self.image = player_img
		self.rect = self.image.get_rect()
		self.rect.center = (WIDTH/2, HEIGHT/2)
		

	def update(self):
			self.rect.x += 5
			
			if self.rect.left > WIDTH:
				self.rect.right = 0




# Initalize pygame and create window
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("My Game")
clock = pygame.time.Clock()
all_sprties = pygame.sprite.Group()


# Set up image folder
game_folder = os.path.dirname(__file__)
img_folder = os.path.join(game_folder, "img")
player_img = pygame.image.load(os.path.join(img_folder,"p1_jump.png")).convert()
player = Player()
all_sprties.add(player)




# Game Loop
running = True
while running:
	# Keep loop running at the right speed
	clock.tick(FPS)
	# Process Input(events)
	for event in pygame.event.get():
		# Check for closing window
		if event.type == pygame.QUIT:
			running = False
	# Update
	all_sprties.update()


	# Draw / Render
	screen.fill(BLACK)
	all_sprties.draw(screen)

	# *After* drawing everything, flip the display
	pygame.display.flip()

pygame.quit()
