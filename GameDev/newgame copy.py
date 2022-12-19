# pygame template - skeleton for a new pygame project
import pygame
import random

WIDTH = 800 # width of our game window 
HEIGHT = 600 # heieght of our game window 
FPS = 30000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000

#define colors
WHITE = (255,255,255)
BLACK = (0,0,0)
RED = (255,0,0)
BLUE = (0,0,255)
GREEN = (0,255,0)

class Player(pygame.sprite.Sprite):
	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.Surface((50, 50))
		self.image.fill(BLUE)
		self.rect = self.image.get_rect()
		self.rect.center = (WIDTH/2, HEIGHT/2)

	def update(self):
			self.rect.x += 15
			
			if self.rect.left > WIDTH:
				self.rect.right = 0

class Player2(pygame.sprite.Sprite):
	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.Surface((50, 50))
		self.image.fill(WHITE)
		self.rect = self.image.get_rect()
		self.rect.center = (HEIGHT/2, WIDTH/2)

	def update(self):
			self.rect.x += 15
			
			if self.rect.left > HEIGHT:
				self.rect.right = 0





# initalize pygame and create window
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("My Game")
clock = pygame.time.Clock()
all_sprties = pygame.sprite.Group()

player = Player()
all_sprties.add(player)
player = Player2()
all_sprties.add(player)

# Game Loop
running = True
while running:
	# keep loop running at the right speed
	clock.tick(FPS)
	# process Input(events)
	for event in pygame.event.get():
		# check for closing window
		if event.type == pygame.QUIT:
			running = False
	# Update
	all_sprties.update()


	# Draw / render
	screen.fill(BLACK)
	all_sprties.draw(screen)

	# *after* drawing everything, flip the display
	pygame.display.flip()

pygame.quit()
