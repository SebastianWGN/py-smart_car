import pygame	
import random

from genAlgorithmFunctions import populate
from models.car import Car
from models.obstacle import Obstacle

#colours
from utils.obstaclesFactory import generateObstacles

grey = (118,119,110)
black = (0,0,0)



#Semilla del random
random.seed(3)

#image assets
carimg = pygame.image.load("assets/icar2.png")	#imagen del carro
backasfalt = pygame.image.load("assets/asfalto.jpg") #imagen del asfalto

backgroundleft=pygame.image.load("assets/left.png")	#imagen del cesped izquierdo
backgroundright=pygame.image.load("assets/right.png")	#imagen del cesped derecho

asfaltLeftLimitX = 330
asfaltRightLimitX = 670

def background(display):
	display.blit(backasfalt, (0, 0))
	display.blit(backgroundleft,(0,0))	    #set left side position of background image at x axis & y axis
	display.blit(backgroundright,(666,0))	#set right side position of background image at x axis & y axis


def crashWithObstacle(obstacle: Obstacle, car: Car) -> bool:
	if car.y < obstacle.y + obstacle.height:  # if obstacle car not pass
		if car.x > obstacle.x and car.x < obstacle.x + obstacle.width \
				or car.x + car.width > obstacle.x and car.x + car.width < obstacle.x + obstacle.width:
			return True
	else:
		return False


def crashWithAsfaltLimit(car: Car, asfaltLimitLeft: float, asfaltLimitRight: float) -> bool:
	if car.x < asfaltLeftLimitX or car.x > asfaltRightLimitX - car.width:
		return True
	else:
		return False

def carMoves(obstacle: Obstacle, car: Car, currentDirection: int):
	if obstacle.y > 0:
		if car.y - (obstacle.y + obstacle.height) < 10:
				car.move(currentDirection)
				return True
	return False

#Logic in game
def game_loop(display):		#all the function are called using this function

	currentGeneration = 1
	car_width = 52
	itMoved = False
	#Generamos la lista de obstaculos
	obstacleList = generateObstacles()
	sizeObstacles = len(obstacleList) #Tamaño de la lista de obstaculos

	# Tamaño de la población
	sizePopulation = 12
	# Indice de la lista de direcciones en ejecución que ira aumentando para acceder a la siguiente lista (Genoma)
	currentDirection = 0

	# Indice del obstáculo que irá aumentando para acceder al siguiente obstáculo
	obstaclesCounter = 0

	# Creamos la población de direcciones inicial
	currentListDirections = populate(sizeObstacles, sizePopulation)

	# Carro y obstáculo inicial
	theCar = Car(475, 540, car_width)


	bumped = False	#if game is not any problem to start
	while not bumped:	#game is start
		for event in pygame.event.get(): 	#if any input is given
			if event.type==pygame.QUIT:		#if quit input is given
			#	bumped=True		#game is stop
				pygame.quit()
				quit()


		if currentDirection < sizePopulation:
			if obstaclesCounter == sizeObstacles:
				currentDirection += 1
				obstaclesCounter = 0
		else:
			currentGeneration += 1
			currentDirection = 0
			newGenerationDirections = populate(sizeObstacles, sizePopulation)
			currentListDirections = newGenerationDirections


		########### MOVE CONDITION FOR THE CAR ###########
		if not itMoved:
			itMoved = carMoves(obstacleList[obstaclesCounter],
					 theCar,
					 currentListDirections[currentDirection][obstaclesCounter])

		################################


		############# DISPLAYS #############
		background(display)

		#Para que me explique pepino la utilidad
		obstacleList[obstaclesCounter].y -= (obstacleList[obstaclesCounter].speed/4)
		obstacleList[obstaclesCounter].draw(display)
		obstacleList[obstaclesCounter].y += obstacleList[obstaclesCounter].speed

		theCar.draw(display)
		################################


		
		######## PASSED OBSTACLE ########

		if obstacleList[obstaclesCounter].y > 600:		#obstacle car pass it without crashed
			# obstacleList[obstaclesCounter].setY(0 - obstacleList[obstaclesCounter].height)	#only one car is crossed
			# obstacleList[obstaclesCounter].setX(random.randrange(355,590,125))	#anthor car is come
			# obstacleList[obstaclesCounter].setObstacleType(random.randrange(0,2))	#diffrent car come
			obstaclesCounter += 1
			itMoved = False



		################################

		#COLOCAR CONDICIÓN DE CREACIÓN DE GENERACIÓN SIGUIENTE

		####### CRASH CONDITIONS #######

		# Car crash with one of the asfalt limits
		crashedWithAsfalt = crashWithAsfaltLimit(theCar, asfaltLeftLimitX, asfaltRightLimitX)

		# Car crash with the obstacle
		crashedWithObstacle = crashWithObstacle(obstacleList[obstaclesCounter], theCar)


		if crashedWithAsfalt or crashedWithObstacle:
			theCar.crash(display)
			obstaclesCounter = 0
			currentDirection += 1

			if currentDirection == sizePopulation:
				currentDirection = 0
				currentGeneration += 1
				newGenerationDirections = populate(sizeObstacles, sizePopulation)
				currentListDirections = newGenerationDirections
			game_loop(display)
		################################



		pygame.display.update()		#update the display	

