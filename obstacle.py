import pygame

pygame.init()	

def gobstacle(obstacle_startx,obstacle_starty, obstacle, display): 	#define obstacle function
	if obstacle == 0:		#at 0 stage
		obstacle_come = pygame.image.load("assets/loli2.png")	#police car2 come
	if obstacle == 1:		#at 1 stage
		obstacle_come = pygame.image.load("assets/loli1.png")	#police car3 come
	if obstacle == 2:
		obstacle_come = pygame.image.load("assets/loli1.png")	#police car1 come

	display.blit(obstacle_come,(obstacle_startx,obstacle_starty))	#display the police car

