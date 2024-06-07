import pygame
from random import randint
pygame.init()


# MUSIC AND SOUNDS
food_eat = pygame.mixer.Sound('snk_food.wav')
bg_music = pygame.mixer.music.load('game_music.wav')


# COLOURS
white = (255,255,255)
black = (0, 0, 0)
red = (255, 0, 0)
lightgreen = (0, 255, 0)
green = (0, 200, 0)
blue = (0, 0, 255)
darkblue = (0, 0, 155)
gray = (180, 184, 181)


# GLOBAL VARIABLES
width, height = 700, 400
screen = pygame.display.set_mode((width, height))
title = pygame.display.set_caption('SNAKE GAME')
clock = pygame.time.Clock()
snk_size = 10


def quitButton(screen, button_text, x_cor, y_cor, fontsize, button_width, button_height):
	font = pygame.font.SysFont("serif", fontsize, 'bold')
	Button = font.render(button_text, True, black)
	rect = pygame.draw.rect(screen, green, [x_cor, y_cor, button_width, button_height])
	screen.blit(Button, [x_cor+int(fontsize/2), y_cor+int(fontsize/4)])
	mouse = pygame.mouse.get_pos()

	# On hovaring the button, the button changes its color from green to lightgreen
	if x_cor < mouse[0] < (x_cor+button_width) and y_cor < mouse[1] < (y_cor+button_height):
		 Button = font.render(button_text, True, black)
		 pygame.draw.rect(screen, lightgreen, [x_cor, y_cor, button_width, button_height])
		 screen.blit(Button, [x_cor+int(fontsize/2), y_cor+int(fontsize/4)])

		# when clicked on the button, the game terminates
		 for event in pygame.event.get():
			 if event.type == pygame.MOUSEBUTTONUP:
				 if event.button == 1:
				 	pygame.quit()
				 	quit()
    	

def playAgainButton(screen, button_text, x_cor, y_cor, fontsize, button_width, button_height):
	font = pygame.font.SysFont("serif", fontsize, 'bold')
	Button = font.render(button_text, True, black)
	pygame.draw.rect(screen, green, [x_cor-5, y_cor, button_width, button_height])
	screen.blit(Button, [x_cor, y_cor+8])
	mouse = pygame.mouse.get_pos() # get mouse coordinates in a tuple form
	
	# On hovaring the button, the button changes its color from green to lightgreen
	if x_cor < mouse[0] < (x_cor+button_width) and y_cor < mouse[1] < (y_cor+button_height):
		 Button = font.render(button_text, True, black)
		 pygame.draw.rect(screen, lightgreen, [x_cor-5, y_cor, button_width, button_height])
		 screen.blit(Button, [x_cor, y_cor+8])

		# when clicked on the button, the gameloop executes and the game starts
		 for event in pygame.event.get():
			 if event.type == pygame.MOUSEBUTTONUP:
				 if event.button == 1:
				 	gameloop()
				 	

def display_text(text, color, x1, y1):
	font = pygame.font.SysFont(None, 30)
	score_text = font.render(text, True, color)
	screen.blit(score_text, [x1, y1])


def plot_snk(screen, color, snk_size, snk_list):
	for x,y in snk_list:
		pygame.draw.rect(screen,color,[x, y, snk_size, snk_size])


def gameloop():
	# Local variables
	x =int(width/2)	# snake head's x - coordinate
	y = int(height/2) # snake head's y - coordinate
	i = 1  		# use to increase fps when score becomes multiple of 100
	val_x = 0	# Velocity at x axis
	val_y = 0	# Velocity at y axis
	score = 0	# score of the player
	food_x = randint(31, width//2) # food x - coordinate
	food_y = randint(31, height//2) # food y - coordinate
	snk_list = []	# empty list which is used as a body of the snake
	snk_length = 1	# snake length
	quit_game = False
	exit = False
	prev_path = '' 	# use to store previous path of the snake
	pygame.mixer.music.play(-1) # plays the music in a loop
	pygame.mixer.music.set_volume(0.4) # set the music volume
	
	while quit_game == False:

		# when player outs
		if exit:
			screen.fill(white) # fill the screen with white colour
			display_text("Game Over!", red, int((width/2)-(width/10)), int((height/2)-(height/4)))
			playAgainButton(screen, 'PLAY AGAIN', 285, 188, 15, 115, 30)
			quitButton(screen, 'QUIT', 297, 140, 20, 80, 30)
			display_text("Your Score: "+str(score), blue, 100, 100) # display the score
			
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					quit_game = True
				elif event.type == pygame.KEYDOWN:
					if event.key == pygame.K_ESCAPE:
						quit_game =True
			pygame.display.update()				
		
		else:
			for event in pygame.event.get(): # getting events
				if event.type == pygame.QUIT: # if quit the screen
						quit_game = True
					
				# when any key is pressed	
				elif event.type == pygame.KEYDOWN: 
					if event.key == pygame.K_ESCAPE: # if the esc key is pressed
						quit_game = True

					# If the left arrow key is pressed and the previous path of the snake is right
					if event.key == pygame.K_LEFT:
						if prev_path != 'right':
							val_x = -10 # decrease the velocity of snake by 10 in x-axis
							val_y = 0 # set the velocity of snake 0 in y-axis, so it can move only in one direction
							prev_path = 'left' # update the prev_path

					# If the right arrow key is pressed and the previous path of the snake is left
					elif event.key == pygame.K_RIGHT:
						if prev_path != 'left':
							val_x = 10 # increase the velocity of snake by 10 in x-axis
							val_y = 0 # set the velocity of snake 0 in y-axis, so it can move only in one direction
							prev_path = 'right' # update the prev_path

					 # If the up arrow key is pressed and the previous path of the snake is down
					elif event.key == pygame.K_UP:
						if prev_path != 'down':
							val_y = -10 # decrease the velocity of snake by 10 in y-axis
							val_x = 0 # set the velocity of snake 0 in x-axis, so it can move only in one direction
							prev_path = 'up' # update the prev_path

					# If the down arrow key is pressed and the previous path of the snake is up
					elif event.key == pygame.K_DOWN:
						if prev_path != 'up':
							val_y = 10 # increase the velocity of snake by 10 in y-axis
							val_x = 0 # set the velocity of snake 0 in x-axis, so it can move only in one direction
							prev_path = 'down' # update the prev_path
							
						
					
			# if the difference between snake head's coordinates and food coordinates are less then 8 that means snake ate the food
			if abs(x-food_x) < 8 and abs(y-food_y) < 8:
				food_eat.set_volume(5) # set the food_eat volume 5
				food_eat.play() # play the food_eat sound
				 
				score += 10 # increase the score by 10
				previous_food = (food_x, food_y) # store the previous food coordinates so that the next food doesn't appear at the same coordinates
				if score > 500: # If the score the below 500, the food appear at center area of the screen
					food_x = randint(31, width - snk_size)
					food_y = randint(31, height - snk_size)
				else: ## Else, the food can appear at any coordinates of the screen
					food_x = randint(60, width//2)
					food_y = randint(60, height//2)
					
				snk_length += 1 # increase the length of the snake by 1
				if (food_x, food_y) == previous_food: # if the current food coordinates match the previous coordinates then increase the current coordinates by 2
					food_x += 2
					food_y += 2

			# add the velocity of snake in its coordinates
			x += val_x
			y += val_y		
				
					
						
			screen.fill(white)
	
			head = [] # create an empty list
			head.append(x) # append snake head's x coordinate
			head.append(y) # append snake head's y coordinate
			snk_list.append(head) # append head into the snake list
		   	
			if len(snk_list) > snk_length: 
				del snk_list[0]

			# plot the snake and food
			plot_snk(screen, darkblue, snk_size, snk_list)
			snk_food = pygame.draw.rect(screen,red,[food_x, food_y, snk_size, snk_size])
			
			# Label the score
			pygame.draw.rect(screen, gray, [0, 0, width, 28])
			game_score("SCORE- "+str(score), red, int((width/2)-45), 5)
			
			# If the snake collides with itself, set the exit -> true
			if head in snk_list[:-1]:
				exit = True
				pygame.mixer.music.stop()

			# If the snake collides with screen corners, set the exit -> true
			elif x<0 or x > width-1 or y<30 or y > height-1:
				exit = True
				pygame.mixer.music.stop()
			
			
			pygame.display.update() # update the screen
			
			# If the score increases by 100 the fps increases by i*2
			if 100*(i-1) <= score <= 100*i:	
				clock.tick(20 + i*2)
				
				# If the score is multiple of 100 the i increases by 1
				if score == (100*i):
					i += 1
							

	pygame.quit()
	quit()
gameloop()	
