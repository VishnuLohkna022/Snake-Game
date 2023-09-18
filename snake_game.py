import pygame
from random import randint
pygame.init()


# MUSIC AND SOUNDS
food_eat = pygame.mixer.Sound('snk_food.wav')
bg_music = pygame.mixer.music.load('hey mama song.mp3')


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
title = pygame.display.set_caption('~ SNAKE GAME ~')
clock = pygame.time.Clock()
snk_size = 10


##############

#################





def quitHomeButtons(screen, button_text, x_cor, y_cor, fontsize, bg_buttonX, bg_buttonY):
	font = pygame.font.SysFont("serif", fontsize, 'bold')
	Button = font.render(button_text, True, black)
	rect = pygame.draw.rect(screen, green, [x_cor, y_cor, bg_buttonX, bg_buttonY])
	screen.blit(Button, [x_cor+int(fontsize/2), y_cor+int(fontsize/4)])
	mouse = pygame.mouse.get_pos()

	if x_cor < mouse[0] < (x_cor+bg_buttonX) and y_cor < mouse[1] < (y_cor+bg_buttonY):
		 Button = font.render(button_text, True, black)
		 pygame.draw.rect(screen, lightgreen, [x_cor, y_cor, bg_buttonX, bg_buttonY])
		 screen.blit(Button, [x_cor+int(fontsize/2), y_cor+int(fontsize/4)])
		 
		 for event in pygame.event.get():
			 if event.type == pygame.MOUSEBUTTONUP:
				 if event.button == 1:
				 	pygame.quit()
				 	quit()
    	

def playAgainButton(screen, button_text, x_cor, y_cor, fontsize, bg_buttonX, bg_buttonY):
	font = pygame.font.SysFont("serif", fontsize, 'bold')
	Button = font.render(button_text, True, black)
	pygame.draw.rect(screen, green, [x_cor-5, y_cor, bg_buttonX, bg_buttonY])
	screen.blit(Button, [x_cor, y_cor+8])
	mouse = pygame.mouse.get_pos()
	
	if x_cor < mouse[0] < (x_cor+bg_buttonX) and y_cor < mouse[1] < (y_cor+bg_buttonY):
		 Button = font.render(button_text, True, black)
		 pygame.draw.rect(screen, lightgreen, [x_cor-5, y_cor, bg_buttonX, bg_buttonY])
		 screen.blit(Button, [x_cor, y_cor+8])
		 
		 for event in pygame.event.get():
			 if event.type == pygame.MOUSEBUTTONUP:
				 if event.button == 1:
				 	gameloop()
				 	
	


def game_score(text, color, x1, y1):
	font = pygame.font.SysFont(None, 30)
	score_text = font.render(text, True, color)
	screen.blit(score_text, [x1, y1])



def plot_snk(screen, color, snk_size, snk_list):
	for x,y in snk_list:
		pygame.draw.rect(screen,color,[x, y, snk_size, snk_size])



def gameloop():
	x =int(width/2)
	y = int(height/2)
	i = 1
	val_x = 0
	val_y = 0
	score = 0
	food_x = randint(31, width/2)
	food_y = randint(31, height/2)
	snk_list = []
	snk_length = 1
	quit_game = False
	exit = False
	prev_path = ''
	pygame.mixer.music.play(-1)				# this is for bg music
	pygame.mixer.music.set_volume(0.4)
	
	while quit_game == False:
		#mouse = pygame.mouse.get_pos()
		#print(mouse)
		
		if exit:
			screen.fill(white)
			game_score("Game Over!", red, int((width/2)-(width/10)), int((height/2)-(height/4)))
			playAgainButton(screen, 'PLAY AGAIN', 285, 188, 15, 115, 30)
			quitHomeButtons(screen, 'QUIT', 297, 140, 20, 80, 30)
			quitHomeButtons(screen, 'HOME', 297, 236, 19, 80, 30)
			game_score("Your Score: "+str(score), blue, 100, 100)
			
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					quit_game = True
				elif event.type == pygame.KEYDOWN:
					if event.key == pygame.K_ESCAPE:
						quit_game =True
			pygame.display.update()				
		
		else:
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
						quit_game = True
							
				elif event.type == pygame.KEYDOWN:
					if event.key == pygame.K_ESCAPE:
						quit_game = True
						
					if event.key == pygame.K_LEFT:
						if prev_path == '' or prev_path == 'up' or prev_path == 'down' or prev_path == 'left':
							val_x = -10
							val_y = 0
							prev_path = 'left'
						break	
					if event.key == pygame.K_RIGHT:
						if prev_path == '' or prev_path == 'up' or prev_path == 'down' or prev_path == 'right':
							val_x = 10
							val_y = 0
							prev_path = 'right'
						break	
					if event.key == pygame.K_UP:
						if prev_path == '' or prev_path == 'left' or prev_path == 'right' or prev_path == 'up':
							val_y = -10
							val_x = 0
							prev_path = 'up'
						break
					if event.key == pygame.K_DOWN:
						if prev_path == '' or prev_path == 'left' or prev_path == 'right' or prev_path == 'down':
							val_y = 10
							val_x = 0
							prev_path = 'down'
							
						
					
			
			if abs(x-food_x) < 8 and abs(y-food_y) < 8: 
				food_eat.set_volume(5)
				food_eat.play()
				
				score += 10
				previous_food = (food_x, food_y)
				if score > 500:
					food_x = randint(31, width)
					food_y = randint(31, height)
				else:
					food_x = randint(60, width/2)
					food_y = randint(60, height/2)
					
				snk_length += 1
				if (food_x, food_y) == previous_food:
					food_x += 2
					food_y += 2
				
			x += val_x
			y += val_y		
				
					
						
			screen.fill(white)
			#pygame.draw.rect(screen, gray, [0, 0, width, 28])
			#game_score("SCORE: "+str(score), red, width-150, 5)
			
			head = []
			head.append(x)
			head.append(y)
			snk_list.append(head)
		   	
			if len(snk_list) > snk_length:
				del snk_list[0]
				
			plot_snk(screen, darkblue, snk_size, snk_list)
			pygame.draw.rect(screen, gray, [0, 0, width, 28])
			game_score("SCORE- "+str(score), red, int((width/2)-45), 5)
			snk_food = pygame.draw.rect(screen,red,[food_x, food_y, snk_size, snk_size])
			
			
			if head in snk_list[:-1]:
				exit = True
				pygame.mixer.music.stop()

			elif x<0 or x > width-1 or y<30 or y > height-1:
				exit = True
				pygame.mixer.music.stop()
			
			
			pygame.display.update()
			if 100*(i-1) <= score <= 100*i:	
				clock.tick(20 + i*2)
				if score == (100*i):
					i += 1
							

	pygame.quit()
	quit()
gameloop()	
	
	
