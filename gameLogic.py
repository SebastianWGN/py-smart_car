import pygame	
import random
from obstacle import gobstacle
from message import message_display

#colours
grey = (118,119,110)	
black = (0,0,0)


#obstacles x
options = [355,475,590]

#image assets
carimg = pygame.image.load("assets/icar2.png")	#load car image
backasfalt = pygame.image.load("assets/asfalto.jpg")

backgroundleft=pygame.image.load("assets/left.png")	#load background left side image
backgroundright=pygame.image.load("assets/right.png")	#load background right side image 

car_width = 52


def crash(display):		#create crash function to display this message
	message_display("Car Crashed", display)	#display this message call the message_display function
	game_loop(display)


def background(display):
	display.blit(backgroundleft,(0,0))	    #set left side position of background image at x axis & y axis 
	display.blit(backgroundright,(666,0))	#set right side position of background image at x axis & y axis

def car(display, x, y):		#create car function
	display.blit(carimg,(x,y))	#set position of car



#Logic in game
def game_loop(display):		#all the function are called using this function
	x=475		#x axis position for car
	y=540		#y axis position of car
	
	x_change=0	#set x position at x axis
	y_change=0	#set y position at y axis
	
	random.seed(1)
	time = 0

	obstaclecar_speed=9	#obstacle car speed
	
	obstacle = 0	#obstacle car is 0 stage
	obstacle_startx=random.randrange(355,590, 80) 	#obstacle car in x axis comes randomly
	obstacle_starty=-600 #obstacle car comes in y axis -600 becuase opposite side
	
	obstacle_width=52 	#obstacle car width
	obstacle_height=100	#obstacle car height

	bumped=False	#if game is not any problem to start
	while not bumped:	#game is start
		for event in pygame.event.get(): 	#if any input is given
			if event.type==pygame.QUIT:		#if quit input is given
			#	bumped=True		#game is stop
				pygame.quit()
				quit()

			if event.type==pygame.KEYDOWN:	#if any key pressed
				if event.key==pygame.K_LEFT:	#if pressed key is left
					x_change=-5		#move left side -5
				if event.key==pygame.K_RIGHT:	#if pressed key is right
					x_change=5		#move right side +5
			if event.type==pygame.KEYUP:	#if key unpressed then
				x_change=0
		x+=x_change

		display.blit(backasfalt, (0,0))	#apply colour to display
		background(display)

		obstacle_starty-=(obstaclecar_speed/4)		#obstacle car speed at y axis
		gobstacle(obstacle_startx,obstacle_starty,obstacle, display)	#call obstacle function
		obstacle_starty+=obstaclecar_speed			#obstacle car speed increse

		car(display, x,y)	#call the function of car
			
		if x<330 or x>670-car_width:		#if car goes out of this range
		#	bumped=True				#stop the game
			crash(display)					#call crash function
		
		#generate obstacles
		if obstacle_starty>600:		#obstacle car pass it without crashed
			obstacle_starty=0-obstacle_height	#only one car is crossed
			obstacle_startx=random.randrange(100)	#anthor car is come 
			print(random.choice(options))
			obstacle=random.randrange(0,2)	#diffrent car come
			time += 1
			print(time)

		if y<obstacle_starty+obstacle_height: #if obstacle car not pass
			if x > obstacle_startx and x < obstacle_startx + obstacle_width or x + car_width > obstacle_startx and x + car_width < obstacle_startx + obstacle_width or x == obstacle_startx and y == obstacle_starty + obstacle_height:
				crash(display)	#crash the car			

		pygame.display.update()		#update the display	

