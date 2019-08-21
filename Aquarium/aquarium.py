'''
19 August 2019. Originally an experiment; wasn't initially meant to be an aquarium.
Will generate a random number of fish, of varying breeds.
'''
import pygame
import random

# Initiate PyGame and setup the window
pygame.init()
win = pygame.display.set_mode((500, 500))
pygame.display.set_caption("Aquarium")

# Load the sound and play on loop
pygame.mixer.music.load("tank.mp3")
pygame.mixer.music.play(-1)


class Fish:
	'''
	The fish
	'''
	def __init__(self, x = 10, y = 10, vx = 5, vy = 5, kind = 0):
		# Position
		self.x = x
		self.y = y
		# Velocities
		self.vx = vx
		self.vy = vy

		# Load sprites depending on type of fish
		left = ["fish1-l.png", "betta-l.png", "angel-l.png", "clown-l.png"]
		right = ["fish1-r.png", "betta-r.png", "angel-r.png", "clown-r.png"]
		width = [60, 60, 50, 60]
		height = [30, 50, 30, 30]

		self.left = pygame.image.load(left[kind])
		self.right = pygame.image.load(right[kind])
		self.w = width[kind]
		self.h = height[kind]

	def draw(self):
		'''
		Draw the character
		'''
		if self.vx > 0:
			win.blit(self.right, (self.x, self.y))
		else:
			win.blit(self.left, (self.x, self.y))

def drawsc():
	'''
	Update the screen
	'''
	win.blit(pygame.image.load("bg.png"), (0, 0)) # Draw the background
	# Draw all fish
	for i in chars:
		i.draw()
	pygame.display.update() # Update the screen

def genfish(num):
	'''
	Generate a specified amount of randomized fish
	'''
	global chars
	chars = list()

	for i in range(num):
		# Add randomized fish
		chars.append(Fish(x = random.randint(0, 440), y = random.randint(0, 450),\
		vx = random.randint(1, 7), vy = random.randint(1, 7), kind = random.randint(0, 3)))

genfish(random.randint(2, 15)) # Generate a random number of fish

while True:
	'''
	The main loop
	'''
	pygame.time.delay(50)

	# Check for quit
	for event in pygame.event.get():
			if event.type == pygame.QUIT:
				quit()

	# Check for edge of screen
	# (Only turns if they haven't already; fish were getting stuck.)
	for i in chars:
		if ((i.x >= 500 - i.w) and (i.vx > 0)) or ((i.x <= 0) and (i.vx < 0)):
			i.vx *= -1
		if ((i.y >= 500 - i.h) and (i.vy > 0)) or ((i.y <= 0) and (i.vy < 0)):
			i.vy *= -1

	# Randomly change direction
	for i in chars:
		if random.randint(0, 99) == 0: # x axis
			i.vx *= -1
		if random.randint(0, 99) == 0: # y axis
			i.vy *= -1

	# Move the character
	for i in chars:
		i.x += i.vx
		i.y += i.vy

	drawsc()
