# pygame template - skeleton for a new pygame project
import pygame
import random
from os import path
import time

WIDTH = 480 # width of our game window 
HEIGHT = 600 # heieght of our game window 
FPS = 60

#define colors
WHITE = (255,255,255)
BLACK = (0,0,0)
RED = (255,0,0)
BLUE = (0,0,255)
GREEN = (0,255,0)


# initalize pygame and create window
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("My Game")
clock = pygame.time.Clock()

snd_dir = path.join(path.dirname(__file__), "snd")
img_dir = path.join(path.dirname(__file__), "img")



player_img = pygame.image.load(path.join(img_dir, "ship.png")).convert()
alien_img = pygame.image.load(path.join(img_dir, "rock.png")).convert()
bullet_img = pygame.image.load(path.join(img_dir, "laser.png")).convert()

#gameover_img = pygame.image.load(path.join(img_dir , "gameover.jpg")).convert()

go_sound = pygame.mixer.Sound(path.join(img_dir, "pew.wav"))

#font_img = pygame.font.match_font('arial')
expl_sounds = pygame.mixer.Sound(path.join(snd_dir, "go1.wav"))
pygame.mixer.music.load(path.join(snd_dir, "space.ogg"))
pygame.mixer.music.set_volume(0.5)

background = pygame.image.load(path.join(img_dir, "starfield.png")).convert()
background_rect = background.get_rect()

font_name = pygame.font.match_font("arial")
def draw_text(surf, text, size, x, y ):
	font = pygame.font.Font(font_name, size)
	text_surface = font.render(text, True, WHITE)
	text_rect = text_surface.get_rect()
	text_rect.midtop = (x,y)
	surf.blit(text_surface, text_rect)





class Player(pygame.sprite.Sprite):
	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
		#self.image = pygame.Surface((50, 40))
		#self.image.fill(BLUE)
		self.image = pygame.transform.scale(player_img, (50,38))
		self.image.set_colorkey(BLACK)
		self.rect = self.image.get_rect()
		self.rect.centerx = WIDTH / 2
		self.rect.bottom = HEIGHT - 10
		self.speedx = 0

	def update(self):
		self.speedx = 0
		keystate = pygame.key.get_pressed()
		if keystate[pygame.K_RIGHT]:
			self.speedx = 8
		if keystate[pygame.K_LEFT]:
			self.speedx = - 8
		self.rect.x += self.speedx
		if self.rect.right > WIDTH:
			self.rect.right = WIDTH
		if self.rect.left < 0:
			self.rect.left = 0

	def go(self):
		bullet = Bullet(self.rect.centerx, self.rect.top)
		all_sprties.add(bullet)
		bullets.add(bullet)
		go_sound.play()


class Mob(pygame.sprite.Sprite):
	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
		#self.image = pygame.Surface((30, 40))
		#self.image.fill(RED)
		self.image = pygame.transform.scale(alien_img , (30,25))
		self.image.set_colorkey(BLACK)
		self.rect = self.image.get_rect()
		self.rect.x = random.randrange(WIDTH - self.rect.width)
		self.rect.y = random.randrange(-100, -40)
		self.speedy = random.randrange(1, 3)
		self.speedx = random.randrange(-3, 3)

	def update(self):
		self.rect.x += self.speedx
		self.rect.y += self.speedy
		if self.rect.top > HEIGHT + 10 or self.rect.left < -25 or self.rect.right > WIDTH + 20:
			self.rect.x = random.randrange(WIDTH - self.rect.width)
			self.rect.y = random.randrange(-100 , -40)
			self.speedy = random.randrange(1, 8)
	


class Bullet(pygame.sprite.Sprite):
	def __init__(self,x,y):
		pygame.sprite.Sprite.__init__(self)
		#self.image = pygame.Surface((10, 20))
		#self.image.fill(WHITE)
		self.image = pygame.transform.scale(bullet_img , (10,30))
		self.image.set_colorkey(BLACK)
		self.rect = self.image.get_rect()
		self.rect.bottom = y
		self.rect.centerx = x
		self.speedy = -10
		

	def update(self):
		self.rect.y += self.speedy
		#Kill if it movies off the top the screen
		if self.rect.bottom < 0:
			self.kill()

all_sprties = pygame.sprite.Group()
mobs = pygame.sprite.Group()
bullets = pygame.sprite.Group()
player = Player()
all_sprties.add(player)

#m = Mob()
#all_sprties.add(player)
#all_sprties.add(m)

for i in range(5):
	m = Mob()
	all_sprties.add(m)
	mobs.add(m)
score = 0
pygame.mixer.music.play(loops=-1)




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
		elif event.type == pygame.KEYDOWN:
			if event.key == pygame.K_SPACE:
				player.go()
	# Update
	all_sprties.update()


	# Check to see if a bullet hit a mob
	hits = pygame.sprite.groupcollide(mobs, bullets, True, True)
	for hit in hits:
		expl_sounds.play()
		score += 1
		m = Mob()
		all_sprties.add(m)
		mobs.add(m)


	# Checks to see if a mob bit the player 
	hits = pygame.sprite.spritecollide(player, mobs, False, False)
	if hits:
		running = False


	# Draw / render
	screen.fill(BLACK)
	screen.blit(background, background_rect)
	draw_text(screen, str(score), 50, WIDTH / 2, 10)

	all_sprties.draw(screen)

	# *after* drawing everything, flip the display
	pygame.display.flip()

pygame.quit()
